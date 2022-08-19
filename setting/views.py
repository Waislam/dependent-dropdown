from django.shortcuts import render
from .models import Division, PostOffice, PostCode, Thana, District
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.

class DistrictList(APIView):
    def post(self, request):
        division = request.data['division']
        district = {}
        if division:
            districts = Division.objects.get(id=division).districts.all()
            district = {d.name:d.id for d in districts}
        return JsonResponse(data=district, safe=False)
class ThanaList(APIView):
    def post(self, request):
        district = request.data['district']
        thana = {}
        if district:
            thanas = District.objects.get(id=district).thanas.all()
            thana = {d.name:d.id for d in thanas}
        return JsonResponse(data=thana, safe=False)
class PostOfficeList(APIView):
    def post(self, request):
        district = request.data['district']
        post_office = {}
        if district:
            post_offices = District.objects.get(id=district).postoffices.all()
            post_office = {d.name:d.id for d in post_offices}
        return JsonResponse(data=post_office, safe=False)

class PostCodeList(APIView):
    def post(self, request):
        post_office = request.data['post_office'] # here post_code is the var from form
        post_code = {}
        if post_office:
            post_codes = PostOffice.objects.get(id=post_office).postcodess.all()
            post_code = {d.name:d.id for d in post_codes}
        return JsonResponse(data=post_code, safe=False)
