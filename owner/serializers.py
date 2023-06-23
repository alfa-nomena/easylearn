from rest_framework import serializers
from .models import User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "is_staff",
            'name',
            'password',
        ]
        extra_kwargs = {
            'password': 
            {
                'write_only': True
            }
        }