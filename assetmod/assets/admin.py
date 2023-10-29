from django.contrib import admin
from .models import Employee, Asset, Repair, Transfer


admin.site.register([Employee, Asset, Repair, Transfer])
