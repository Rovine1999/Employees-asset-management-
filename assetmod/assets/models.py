from django.db import models
from django.contrib.auth.models import User

#TimeStampedModel is an abstract model that provides self-updating created and modified fields.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #ordering is used to order the results of a query
    class Meta:
        ordering = ['-id']
        abstract = True

#Employee model is used to store employee details
class Employee(TimeStampedModel):
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    employee_no = models.CharField(max_length=50, blank=True, null=True)

#Asset model is used to store asset details
class Asset(TimeStampedModel):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    serial_no = models.CharField(max_length=100, blank=True, null=True)

#Repair model is used to store repair details
class Repair(TimeStampedModel):
    asset = models.ForeignKey(Asset, blank=False, null=False, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=100, blank=False, null=False)
    entry_date= models.DateTimeField(auto_created=True)
    exit_date= models.DateTimeField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    
#Transfer model is used to store transfer details
class Transfer(TimeStampedModel):
    old_employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.SET_NULL, related_name='old_employee')
    current_employee = models.ForeignKey(Employee, blank=False,null=False, on_delete=models.CASCADE, related_name='new_employee')
    asset = models.ForeignKey(Asset, blank=False, null=False, on_delete=models.CASCADE)
