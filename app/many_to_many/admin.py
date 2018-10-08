from django.contrib import admin

# Register your models here.
from .models import Topping, Pizza

admin.site.register(Topping)
admin.site.register(Pizza)
