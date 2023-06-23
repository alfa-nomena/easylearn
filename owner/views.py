from .models import Owner
from rest_framework import generics
from .serializers import OwnerSerializer, OwnerCreateSerializer
from django.contrib.auth.models import User



class OwnerView:
    serializer_class = OwnerSerializer
    queryset = Owner.objects.all()

class OwnerSingleView(OwnerView):
    lookup_field = "public_id"
    

# Get methods
class OwnerDetailView(OwnerSingleView, generics.RetrieveAPIView):
    pass


class OwnerListView(OwnerView, generics.ListAPIView):
    pass
    
# Post methods
class OwnerCreateView(OwnerView, generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = OwnerCreateSerializer
    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception = True):
            data = serializer.validated_data
            user = User.objects.create(
                username=data.get('username'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                password=data.get('password'),
            )
        
            owner = Owner(user=user)
        return owner.save()
# Put methods
class OwnerUpdateView(OwnerSingleView, generics.UpdateAPIView):
    pass

# Delete methods
class OwnerDeleteView(OwnerSingleView, generics.DestroyAPIView):
    pass