"""SampleClassSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from course_reviews import views
from django.conf.urls import url


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'course', views.CourseViewSet)
router.register(r'review', views.ReviewsViewSet)
router.register(r'department', views.DepartmentsViewSet)

urlpatterns = [
    path('course_reviews/', include('course_reviews.urls')),
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^(?!ng/).*$', views.HomePageView.as_view(), name="angular_app"),
    url(r'^(?P<path>.*)/$', views.index),
]
