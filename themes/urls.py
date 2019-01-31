from django.urls import path, include
from . import views
from rest_framework import routers	


urlpatterns = [
	path('theme/', views.ThemeFeed.as_view()),
	path('theme/details/<int:id>/', views.ThemeNameFilter.as_view()),
	path('theme/cart/<int:id>/', views.ThemeCart.as_view()),

]