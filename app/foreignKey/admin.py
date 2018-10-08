from django.contrib import admin

# Register your models here.
from .models import Manufacturer, Car

admin.site.register(Manufacturer)
admin.site.register(Car)
