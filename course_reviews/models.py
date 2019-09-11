import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=500)
    course_number = models.IntegerField(default=0)
    department = ArrayField(models.CharField(max_length=500, blank=True), default=[])
    uuid = models.CharField(max_length=100, blank=False, null=False, primary_key=True, unique=True)
    credits = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=15000, blank=True)
    prereq = models.CharField(max_length=500, blank=True)
    ethnicStudies = models.BooleanField(default=False)
    genEd = ArrayField(models.CharField(max_length=100, blank=True), default=[])
    breadth = ArrayField(models.CharField(max_length=100, blank=True), default=[])
    level = models.CharField(max_length=100, blank=True)
    lasCredit = models.BooleanField(default=False)
    typicallyOffered = ArrayField(models.CharField(max_length=100, blank=True), default=[])

    def __str__(self):
        return self.course_name


class Review(models.Model):
    course = models.ForeignKey(Course, related_name='course_reviews', on_delete=models.CASCADE, to_field='uuid')
    review_text = models.CharField(max_length=5000)
    difficulty_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    interest_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    success_tips_text = models.CharField(max_length=5000)
    date_posted = models.DateTimeField(datetime.now())
    professor = models.CharField(max_length=100)

    def __str__(self):
        return self.review_text





