from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics
from .permissions import *
from rest_framework import authentication



class CourseView:
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsStaffEditor]
    authentication_classes = [
        authentication.TokenAuthentication,
        # authentication.SessionAuthentication
    ]
    
class CourseSingleView(CourseView):
    lookup_field = "public_id"
    

# Get methods
class CourseDetailView(CourseSingleView, generics.RetrieveAPIView):
    pass


class CourseListView(CourseView, generics.ListAPIView):
    pass
    
# Post methods
class CourseCreateView(CourseView, generics.CreateAPIView):
    pass

# Put methods
class CourseUpdateView(CourseSingleView, generics.UpdateAPIView):
    pass

# Delete methods
class CourseDeleteView(CourseSingleView, generics.DestroyAPIView):
    pass