from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NameClassSerializer
from .models import NameAndClass
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from .pagination import CustomPagination
# Create your views here.


# class ListApiViewLi(APIView, PageNumberPagination):
#     page_size = 3
#     # page_query_param = 'p'
#     page_size_query_param = 'records'
#
#     def get(self, request, formate=None):
#         list_li = NameAndClass.objects.all()
#         result = self.paginate_queryset(list_li, request, view=self)
#         serializer = NameClassSerializer(result, many=True)
#         return self.get_paginated_response(serializer.data)


class ListApiViewLi(APIView, CustomPagination):

    def get(self, request, formate=None):
        list_li = NameAndClass.objects.all()
        result = self.paginate_queryset(list_li, request, view=self)
        serializer = NameClassSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)




