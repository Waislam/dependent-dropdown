from rest_framework.mixins import ListModelMixin
from .pagination import CustomPagination
from rest_framework.response import Response


class CustomListModelMixin(ListModelMixin, CustomPagination):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset, request)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

