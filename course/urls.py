from . import views
from django.urls import path


app_name="course"
urlpatterns = [
    path("get/one/<str:public_id>", views.CourseDetailViewMixin.as_view(), name="get-one"),
    path("get/all", views.CourseListViewMixin.as_view(), name="get-all"),
    path("create", views.CourseCreateViewMixin.as_view(), name="create"),
    path("edit/<str:public_id>", views.CourseUpdateViewMixin.as_view(), name="edit"),
    path("delete/<str:public_id>", views.CourseDeleteViewMixin.as_view(), name="delete"),
]
