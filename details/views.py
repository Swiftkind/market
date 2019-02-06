from django.shortcuts import render
from themes.models import Review, Theme
from users.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from .serializers import ReviewSerializer
from rest_framework.authtoken.models import Token


class CreateReview(APIView):
	"""create a review on a post
	"""
	permission_classes = (AllowAny,)
	
	def post(self,request,*args,**kwargs):
		token = self.request.data.get('token')

		self.request.data['user'] = Token.objects.get(key=token).user_id
		self.request.data['theme'] = self.request.data.get('theme_id')
		
		serializer = ReviewSerializer(
			data=self.request.data)
		
		serializer.is_valid(raise_exception=True)
		serializer.save()
		
		return Response({'success': 'Review created!'}, status=200)

		


		