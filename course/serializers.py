from rest_framework import serializers

from .models import Course




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "public_id",
            'title',
            'content',
            "date_posted",
        ]
        