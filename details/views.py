from django.shortcuts import render
from themes.models import Review, Theme
from users.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from .serializers import ReviewSerializer
from rest_framework.authtoken.models import Token
from django.views.generic import View
from io import StringIO
from zipfile import ZipFile
from django.conf import settings
import os


class CreateReview(APIView):
    """create a review on a post
    """
    permission_classes = (AllowAny,)
    sum_values = 0

    def post(self,request,*args,**kwargs):
        """
        """
        token = request.data.get('token')

        request.data['user'] = Token.objects.get(key=token).user_id
        request.data['theme'] = request.data.get('theme_id')
        
        serializer = ReviewSerializer(
            data=request.data)
        
        """save review after validation
        """
        serializer.is_valid(raise_exception=True)
        serializer.save()

        """get average rating of the theme between the ratings of the reviews
        """
        theme_rating = Theme.objects.get(id=request.data.get('theme_id'))
        reviews_rating = Review.objects.filter(theme_id=request.data.get('theme_id')).values('rating')
        list_values = list(reviews_rating)
        average_rating = self.get_average_rating(list_values,'rating')

        """update theme with new rating
        """
        theme_rating.rating = int(average_rating)
        theme_rating.save()

        return Response({'success': 'Review created!'}, status=200)

    
    def get_average_rating(self,list_values,key):
        
        for rating in list_values:
            self.sum_values += rating[key]
        return self.sum_values/len(list_values)


class DownloadTheme(APIView):
    """download theme view
    """ 
    permission_classes = (AllowAny,)

    def get(self,*args,**kwargs):
        """
        increment downloads for theme
        """
        theme = Theme.objects.get(id=kwargs.get('theme_id'))
        theme.downloads+=1
        theme.save()
        
        return Response({'increment': 'Theme has '+ theme['downloads']},status=200)
        






        


        