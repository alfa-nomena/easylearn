from . import views
from django.urls import path


app_name="course"
urlpatterns = [
    path("get/one/<str:public_id>", views.CourseDetailView.as_view(), name="get-one"),
    path("get/all", views.CourseListView.as_view(), name="get-all"),
    path("create", views.CourseCreateView.as_view(), name="create"),
    path("edit/<str:public_id>", views.CourseUpdateView.as_view(), name="edit"),
    path("delete/<str:public_id>", views.CourseDeleteView.as_view(), name="delete"),
]
