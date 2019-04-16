import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Course(models.Model):
    course_name = models.CharField(max_length=500)
    department = models.CharField(max_length=500)
    course_number = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=5000)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.review_text






