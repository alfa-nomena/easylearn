from .serializers import CourseSerializer
from .models import Course
from rest_framework import generics
from .permissions import *




class CourseViewMixin:
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]
    
class CourseSingleViewMixin(CourseViewMixin):
    lookup_field = "public_id"
    

# Get methods
class CourseDetailViewMixin(CourseSingleViewMixin, generics.RetrieveAPIView):
    pass


class CourseListViewMixin(CourseViewMixin, generics.ListAPIView):
    pass
    
# Post methods
class CourseCreateViewMixin(CourseViewMixin, generics.CreateAPIView):
    pass

# Put methods
class CourseUpdateViewMixin(CourseSingleViewMixin, generics.UpdateAPIView):
    pass

# Delete methods
class CourseDeleteViewMixin(CourseSingleViewMixin, generics.DestroyAPIView):
    pass