from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (Theme, Review, Thumbnail, Screenshot, Browser, Category, Topic)


class ThemeAdmin(admin.ModelAdmin):
	"""themes admin
	"""
	model = Theme

	list_display = (
		'name',
		'description',
		'rating',
		'price',
		'discount',
		'version',
	)


class ReviewAdmin(admin.ModelAdmin):
	"""review admin
	"""
	model = Review

	list_display = (
		'user',
		'rating',
		'comment'
	)


class ThumbnailAdmin(admin.ModelAdmin):
	"""thumbnail admin
	"""
	model = Thumbnail

	list_display = (
		'theme',
		'thumbnail',
	)

class ScreenshotAdmin(admin.ModelAdmin):
	"""screenshot admin
	"""
	model = Screenshot

	list_display = (
		'theme',
		'image',
	)


class BrowserAdmin(admin.ModelAdmin):
	"""browsers admin
	"""
	model = Browser

	list_display = (
		'browser',
	)


class CategoryAdmin(admin.ModelAdmin):
	"""category admin
	"""
	model = Category

	list_display = (
		'category',
	
	)

class TopicAdmin(admin.ModelAdmin):
	"""topic admin
	"""
	model = Topic

	list_display = (
		'topic',
	)




admin.site.register(Theme, ThemeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)
admin.site.register(Browser, BrowserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
