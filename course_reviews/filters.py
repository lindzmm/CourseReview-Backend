from django_filters import rest_framework as filters
import django_filters
from course_reviews.models import Course


class CourseFilter(filters.FilterSet):
    course_number = django_filters.CharFilter(lookup_expr="iexact")
    course_name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Course
        fields = ['course_number', 'course_name']