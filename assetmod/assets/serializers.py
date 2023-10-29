from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Employee, Asset, Repair, Transfer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        init_data = self.initial_data
        _password = init_data.get('password', init_data.get('username'))
        validated_data['password'] = make_password(_password)
        return super().create(validated_data=validated_data)


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__'


class RepairSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repair
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        fields = '__all__'

