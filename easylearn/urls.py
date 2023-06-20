from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include("course.urls")),
    path('owner/', include("owner.urls")),
    path('comments/', include("comment.urls")),
    path('login', obtain_auth_token),
    path("", lambda x: redirect("course:home")),
]
