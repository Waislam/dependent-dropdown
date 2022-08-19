from .models import NameAndClass
from rest_framework import serializers


class NameClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = NameAndClass
        fields = ['id', 'name', 'class_name']