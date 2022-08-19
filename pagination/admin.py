from django.contrib import admin
from .models import NameAndClass
# Register your models here.

@admin.register(NameAndClass)
class NameModelView(admin.ModelAdmin):
    list_display = ['id', 'name', 'class_name']
