from django.db import models
from users.models import User


class Themes(models.Model):
	"""
	themes
	"""
	owners = models.ManyToManyField(User,blank=True)
	name = models.CharField(max_length=100)
	description = models.TextField()
	rating = models.IntegerField()
	price = models.FloatField()
	discount = models.FloatField(blank=True)
	thumbnail = models.ImageField(upload_to='thumbnails')
	screenshot = models.ManyToManyField('themes.Screenshot',blank=True)
	version = models.FloatField()
	theme_type = models.CharField(max_length=100)
	bootstrap = models.CharField(max_length=100)
	layouts = models.CharField(max_length=50)
	browsers = models.ManyToManyField('themes.Browsers',blank=True)
	uses_less = models.BooleanField()
	uses_sass = models.BooleanField()
	category = models.ForeignKey('themes.Category',on_delete=models.CASCADE,blank=True)
	topic = models.ForeignKey('themes.Topic',on_delete=models.CASCADE,blank=True)
	labels = models.CharField(max_length=100)
	released = models.CharField(max_length=100)
	review = models.ManyToManyField('themes.Review',blank=True)


class Review(models.Model):
	"""
	review
	"""
	
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	rating = models.IntegerField(default=0)
	comment = models.TextField(blank=True)


class Screenshot(models.Model):
	"""
	screenshot
	"""

	image = models.ImageField(upload_to='screenshots')


class Browsers(models.Model):
	"""
	browsers
	"""
	browser = models.CharField(max_length=100)


class Category(models.Model):
	"""
	category
	"""
	category = models.CharField(max_length=100)


class Topic(models.Model):
	"""
	topic
	"""
	topic = models.CharField(max_length=100)


