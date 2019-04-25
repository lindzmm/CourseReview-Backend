import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=500)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    department = models.ForeignKey(Department, related_name="department_courses", on_delete=models.CASCADE)
    course_name = models.CharField(max_length=500)
    course_number = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name


class Review(models.Model):
    course = models.ForeignKey(Course, related_name='course_reviews', on_delete=models.CASCADE)
    review_text = models.CharField(max_length=5000)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.review_text






