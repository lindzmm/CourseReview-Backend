from course_reviews.models import Course, Review, Department
from rest_framework import serializers


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    department_courses = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='course-detail')

    class Meta:
        model = Department
        fields = ('department_name', 'id', 'department_courses')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    course_reviews = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='review-detail')

    class Meta:
        model = Course
        fields = ('id', 'url', 'course_name', 'course_number', 'department', 'course_reviews')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('url', 'course', 'review_text', 'rating')
