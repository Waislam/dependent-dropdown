from django.contrib import admin

from searching.models import Students


# Register your models here.

@admin.register(Students)
class StudentAdminView(admin.ModelAdmin):
    list_display = ['id', 'name', 'student_id', 'class_name', 'roll']
