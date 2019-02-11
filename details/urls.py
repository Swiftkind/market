from django.urls import path, include
from . import views

urlpatterns = [
	path('createReview/', views.CreateReview.as_view()),
	path('download/<int:theme_id>/',views.DownloadTheme.as_view()),
]