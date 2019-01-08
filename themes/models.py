from django.db import models
from users.models import User
from market import settings

def thumbnail_upload_path(instance, filename):
	return 'images/{0}/thumbnail/{1}'.format(instance.theme.id, filename)

def screenshot_upload_path(instance, filename):
	return 'images/{0}/screenshot/{1}'.format(instance.theme.id, filename)


class Theme(models.Model):
	"""themes
	"""
	owners = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
	name = models.CharField(max_length=100)
	description = models.TextField()
	rating = models.IntegerField(blank=True)
	price = models.FloatField()
	discount = models.FloatField(blank=True)
	version = models.CharField(max_length=50, blank=True)
	theme_type = models.CharField(max_length=100)
	bootstrap = models.CharField(max_length=100)
	layouts = models.CharField(max_length=50)
	browser = models.ManyToManyField('themes.Browser', blank=True)
	uses_less = models.BooleanField()
	uses_sass = models.BooleanField()
	category = models.ForeignKey('themes.Category', on_delete=models.CASCADE, blank=True)
	topic = models.ForeignKey('themes.Topic', on_delete=models.CASCADE, blank=True)
	labels = models.CharField(max_length=100)
	released = models.CharField(max_length=100)
	review = models.ForeignKey('themes.Review', on_delete=models.CASCADE, blank=True)


class Review(models.Model):
	"""review
	"""
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	rating = models.IntegerField(default=0)
	comment = models.TextField(blank=True)


class Screenshot(models.Model):
	"""screenshot
	"""
	theme = models.ForeignKey('themes.Theme', on_delete=models.CASCADE)
	image = models.ImageField(upload_to=screenshot_upload_path)


class Thumbnail(models.Model):
	"""thumbnail
	"""
	theme = models.ForeignKey('themes.Theme', on_delete=models.CASCADE)
	thumbnail = models.ImageField(upload_to=thumbnail_upload_path)


class Browser(models.Model):
	"""browsers
	"""
	browser = models.CharField(max_length=100)


class Category(models.Model):
	"""category
	"""
	category = models.CharField(max_length=100)


class Topic(models.Model):
	"""topic
	"""
	topic = models.CharField(max_length=100)


