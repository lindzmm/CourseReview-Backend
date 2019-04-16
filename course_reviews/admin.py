from django.contrib import admin

from .models import Question, Course

admin.site.register(Question)
admin.site.register(Course)
