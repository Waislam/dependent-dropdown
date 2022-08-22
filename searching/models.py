from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50)
    roll = models.CharField(max_length=50)
