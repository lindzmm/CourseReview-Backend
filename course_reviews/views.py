from django.http import HttpResponse

from .models import Course, Review
from rest_framework import viewsets
from course_reviews.serializers import CourseSerializer, ReviewSerializer
from django.shortcuts import render
from django.views.generic.base import TemplateView


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


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