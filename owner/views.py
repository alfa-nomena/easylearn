from .models import User
from rest_framework import generics
from .serializers import OwnerSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class OwnerView:
    serializer_class = OwnerSerializer
    queryset = User.objects.all()

class OwnerSingleView(OwnerView):
    lookup_field = "id"
    

# Get methods
class OwnerDetailView(OwnerSingleView, generics.RetrieveAPIView):
    pass


class OwnerListView(OwnerView, generics.ListAPIView):
    pass
    
# Post methods
class OwnerCreateView(OwnerView, generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = OwnerSerializer
# Put methods
class OwnerUpdateView(OwnerSingleView, generics.UpdateAPIView):
    pass

# Delete methods
class OwnerDeleteView(OwnerSingleView, generics.DestroyAPIView):
    pass