from django.contrib.auth.models import User
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Employee, Asset, Repair, Transfer
from datetime import timedelta

# TimeStampedModel is an abstract model that provides self-updating created and modified fields.
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
#function to validate data from the user
    def create(self, validated_data):
        init_data = self.initial_data
        _password = init_data.get('password', init_data.get('username'))
        validated_data['password'] = make_password(_password)
        return super().create(validated_data=validated_data)

#Employee serializer is used to store employee details
class EmployeeSerializer(serializers.ModelSerializer):

#function to validate data from the user entered
    class Meta:
        model = Employee
        fields = '__all__'

#Asset serializer is used to store asset details
class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__'

#Repair serializer is used to store repair details
class RepairSerializer(serializers.ModelSerializer):
    time_spent_in_garage = serializers.SerializerMethodField() # SerializerMethodField is used to add a custom field to the serializer for thetime spent in garage

    class Meta:
        model = Repair
        fields = '__all__'
#function to validate data from the user entered
    def validate(self, data):
        if data.get('entry_date') and data.get('exit_date'):
            if data['entry_date'] >= data['exit_date']:
                raise ValidationError("Entry date must be before exit date.")
        return data
#
    def get_time_spent_in_garage(self, obj):
        entry_date = obj.entry_date
        exit_date = obj.exit_date

        if entry_date and exit_date:
            time_spent = exit_date - entry_date
            days = time_spent.days
            hours, remainder = divmod(time_spent.seconds, 3600)
            minutes, _ = divmod(remainder, 60)

            return f"{days} days, {hours} hours, {minutes} minutes"
        else:
            return "Time in garage not calculated"

#Transfer serializer is used to store transfer details from one employee to another
class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        fields = '__all__'

