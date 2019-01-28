from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
