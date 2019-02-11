from django.urls import path, include
from . import views

urlpatterns = [
	path('createReview/', views.CreateReview.as_view()),
]