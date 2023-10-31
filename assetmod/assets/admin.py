from django.contrib import admin
from .models import Employee, Asset, Repair, Transfer

#Registering models in admin panel to view and edit data from admin panel
admin.site.register([Employee, Asset, Repair, Transfer])
