from .models import Students
import django_filters


class StudentFilter(django_filters.FilterSet):
    # user__phone = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Students
        fields = ['student_id', 'name', 'class_name', 'roll']