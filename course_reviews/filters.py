from django_filters import rest_framework as filters
import django_filters
from course_reviews.models import Course
from django.contrib.postgres.fields import ArrayField


class CharInFilter(django_filters.CharFilter):
    pass


class CourseFilter(filters.FilterSet):
    course_number = django_filters.CharFilter(lookup_expr="iexact")
    course_name = django_filters.CharFilter(lookup_expr="iexact")
    credits = django_filters.CharFilter(lookup_expr="iexact")
    ethnicStudies = django_filters.BooleanFilter()
    level = django_filters.CharFilter(lookup_expr="iexact")
    lasCredit = django_filters.BooleanFilter()
    department = CharInFilter(lookup_expr='icontains')

    class Meta:
        model = Course
        fields = ['course_number', 'course_name', 'department', 'credits', 'ethnicStudies', 'genEd', 'breadth', 'level',
                  'lasCredit', 'typicallyOffered']
        filter_overrides = {
            ArrayField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                },
            },
        }

