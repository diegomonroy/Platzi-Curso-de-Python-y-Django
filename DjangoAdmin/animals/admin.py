from django.contrib import admin
from .models import Animal

# Register your models here.

@admin.register(Animal)
class Animals(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name')