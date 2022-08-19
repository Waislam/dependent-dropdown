from django.urls import path
from .views import ListApiViewLi

urlpatterns = [
    path('list/', ListApiViewLi.as_view()),
]