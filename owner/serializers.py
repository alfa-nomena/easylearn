from rest_framework import serializers
from .models import Owner
from rest_framework.validators import UniqueValidator
from .models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            "public_id",
            'name',
            'user',
        ]
    
        
class OwnerCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': 
            {
                'write_only': True
            },
            "username":
            {
                'validators': [
                    UniqueValidator(
                        queryset=Owner.objects.all()
                    )
                ]
            }
        }
        