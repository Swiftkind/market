from rest_framework import serializers
from themes.models import Review
from django.utils.translation import ugettext_lazy as _


class ReviewSerializer(serializers.ModelSerializer):
	"""review 
	"""
	class Meta:
		model = Review
		fields = (
			'theme',
			'user',
			'comment',
			'rating',
		)

	def validate(self,data):
		comment = data.values

		if not comment:
			msg = 'Please enter a comment'

		return data



