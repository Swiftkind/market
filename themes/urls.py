from django.urls import path, include
from . import views

urlpatterns = [
	path('theme/', views.ThemeFeed.as_view()),
	path('theme/details/<int:id>/', views.ThemeNameFilter.as_view()),
	path('theme/cart/<int:id>/', views.ThemeCart.as_view()),
	path('theme/category/',views.CategoryView.as_view()),
]