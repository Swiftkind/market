from rest_framework import serializers
from .models import (Theme, Thumbnail, Screenshot, Review, Browser, Category, Topic, Label, License)


class ThemeDetailSerializer(serializers.ModelSerializer):
	"""theme serializer
	"""
	class Meta:
		model = Theme
		fields = '__all__'


class ThumbnailSerializer(serializers.ModelSerializer):
	"""thumbnail serializer
	"""
	class Meta:
		model = Thumbnail
		fields = (
			'pk',
			'theme',
			'thumbnail'
		)

class CategorySerializer(serializers.ModelSerializer):
	"""category serializer
	"""
	class Meta:
		model = Category
		fields = (
			'pk',
			'category',
		)


class TopicSerializer(serializers.ModelSerializer):
	"""topic serializer
	"""
	class Meta:
		model = Topic
		fields = (
			'pk',
			'topic',
		)


class LicenseSerializer(serializers.ModelSerializer):
	"""license serializer
	"""
	class Meta:
		model = License
		fields = (
			'pk',
			'license',
		)

