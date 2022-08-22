from django_filters.rest_framework import DjangoFilterBackend # this is Django-filter
from rest_framework.filters import SearchFilter # this is search


class CustomeSearch(SearchFilter):
    """Customized search fields, it makes it dynamic"""
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])