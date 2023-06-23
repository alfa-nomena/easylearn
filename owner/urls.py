from .import views
from django.urls import path


app_name="owner"
urlpatterns = [
    path("create", views.OwnerCreateView.as_view(), name="create"),
    path("get/all", views.OwnerListView.as_view(), name="get-all"),
    path("get/one/<str:id>", views.OwnerDetailView.as_view(), name="get-one"),
    path("update/<str:id>", views.OwnerUpdateView.as_view(), name="create"),
    path("delete/<str:id>", views.OwnerDeleteView.as_view(), name="delete"),
]
