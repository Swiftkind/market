from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import (
	Themes, Review, 
	Screenshot, Browsers, 
	Category, Topic
)


class ThemesAdmin(UserAdmin):
	"""
	themes admin
	"""
	model = Themes

	list_display = (
		'name','description',
		'rating','price',
		'discount','version',
	)


class ReviewAdmin(UserAdmin):
	"""
	review admin
	"""
	model = Review

	list_display = (
		'name',
		'rating',
		'comment'
	)


class ScreenshotAdmin(UserAdmin):
	"""
	screenshot admin
	"""
	model = Screenshot

	list_display = (
		'image',
	)


class BrowsersAdmin(UserAdmin):
	"""
	browsers admin
	"""
	model = Browsers

	list_display = (
		'browser',
	)


class CategoryAdmin(UserAdmin):
	"""
	category admin
	"""
	model = Category

	list_display = (
		'category',
	
	)

class TopicAdmin(UserAdmin):
	"""
	topic admin
	"""
	model = Topic

	list_display = (
		'topic'
	)


# Register your models here.
admin.site.register(Themes)
admin.site.register(Review)
admin.site.register(Screenshot)
admin.site.register(Browsers)
admin.site.register(Category)
admin.site.register(Topic)
