from django.urls import path
from .views import *

urlpatterns = [
    path('district/', DistrictList.as_view()),
    path('thana/', ThanaList.as_view()),
    path('post-office/', PostOfficeList.as_view()),
    path('post-code/', PostCodeList.as_view()),

]