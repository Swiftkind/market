from django.urls import path, include
from . import views

urlpatterns = [
	path('theme/homepage/<str:auth>/', views.ThemeFeed.as_view()),
	path('theme/details/<int:id>/', views.ThemeNameFilter.as_view()),
	path('theme/cart/<int:id>/', views.ThemeCart.as_view()),
	path('theme/category/',views.CategoryView.as_view()),
	path('theme/edit_license/', views.EditLicense.as_view()),
	path('theme/subscribe/', views.Subscribe.as_view()),
]