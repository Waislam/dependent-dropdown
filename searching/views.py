from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .customsearch import CustomeSearch
from rest_framework import mixins, generics
from pagination.customlistmixin import CustomListModelMixin
from searching.models import Students
from .filters import StudentFilter


# Create your views here.

# class StudentListView(ListAPIView):
#     """search and filter usages"""
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['name', 'student_id', 'class_name', 'roll']
#     search_fields = ['^name', 'student_id', 'class_name', 'roll']


# class StudentListView(ListAPIView):
#     """used customized Searchfilter namely CustomeSearch"""
#     """ serach url : http://127.0.0.1:8000/api/searching/students/?search=name2&search_fields=name"""
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [CustomeSearch]


# class StudentView(APIView):
#
#     def get(self, request, formate=None):
#         students = Students.objects.all()
#         filter_backends = [DjangoFilterBackend, SearchFilter]
#         # filterset_fields = ['name', 'student_id', 'class_name', 'roll']
#         search_fields = ['^name', 'student_id', 'class_name', 'roll']

class StudentListView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """used customized ListModelMixin with Customized pagination and custom search"""

    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['student_id', 'name']


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Method to create student api """
        return self.create(request, *args, **kwargs)