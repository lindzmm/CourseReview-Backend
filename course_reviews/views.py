from django.http import HttpResponse

from .models import Course, Review
from rest_framework import viewsets
from course_reviews.serializers import CourseSerializer, ReviewSerializer
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .filters import CourseFilter
from rest_framework import generics
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_class = CourseFilter


class ReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    name = 'review-detail'


def index(request):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)




    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Course.objects.all()
    #     number = self.request.query_params.get('course_number')
    #     if number:
    #         queryset = queryset.filter(course_number=number)
    #     return queryset
