from course_reviews.models import Course, Review
from rest_framework import serializers


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    course_reviews = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name='review-detail')

    class Meta:
        model = Course
        fields = ('uuid', 'url', 'course_name', 'course_number', 'department', 'course_reviews', 'credits',
                  'description', 'prereq',
                  'ethnicStudies', 'genEd', 'breadth', 'level', 'lasCredit', 'typicallyOffered')


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('url', 'course', 'review_text', 'difficulty_rating', 'interest_rating', 'success_tips_text',
                  'date_posted', 'professor')
