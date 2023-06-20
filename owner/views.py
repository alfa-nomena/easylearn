from .models import Owner
from rest_framework import generics
from .serializers import OwnerSerializer



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
    pass

# Put methods
class OwnerUpdateView(OwnerSingleView, generics.UpdateAPIView):
    pass

# Delete methods
class OwnerDeleteView(OwnerSingleView, generics.DestroyAPIView):
    pass