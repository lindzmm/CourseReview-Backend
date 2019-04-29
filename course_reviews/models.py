import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=500)
    course_number = models.IntegerField(default=0)
    uuid = models.CharField(max_length=100, blank=False, null=False, primary_key=True, unique=True)

    def __str__(self):
        return self.course_name


class Review(models.Model):
    course = models.ForeignKey(Course, related_name='course_reviews', on_delete=models.CASCADE, to_field='uuid')
    review_text = models.CharField(max_length=5000)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.review_text






