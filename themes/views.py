from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from .models import (Theme, Thumbnail, Screenshot, Review, Browser, Category, Topic, Label,)
from .serializers import (ThemeDetailSerializer, ThumbnailSerializer, CategorySerializer, TopicSerializer,)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from itertools import chain 
import json




class ThemeFeed(APIView):
    """themes home
    """
    queryset = Theme.objects.all()
    permission_classes = (AllowAny,)

    def get(self,request,*args,**kwargs):
        thumbnail = Thumbnail.objects.all()
      
        data = self.queryset.filter(
            id__in=thumbnail.values('theme_id')
            ).values('id','name','rating','price','thumbnail__thumbnail')

        return Response({
            'data': list(data),
        }, status=200)


class ThemeNameFilter(APIView):
    """themes details
    """
    permission_classes = (AllowAny,)

    def get(self,request,*args,**kwargs):
        theme = Theme.objects.get(id=kwargs['id'])
        review = Review.objects.filter(theme_id=theme.id).values('rating','comment','date_created','user__first_name','user__last_name')
        screenshot = Screenshot.objects.filter(theme_id=theme.id).values()
        thumbnail = Thumbnail.objects.get(theme_id=theme.id)
        browser = theme.browser.all().values()
        category = Category.objects.get(id=theme.category_id)
        topic = Topic.objects.get(id=theme.topic_id)
        label = theme.labels.all().values()

        browser_s = {'browser':list(browser)}
        screenshot_s = {'screenshot':list(screenshot)}
        label_s = {'label':list(label)}
        review_s = {'review':list(review)}

        theme_s = ThemeDetailSerializer(theme).data
        theme_s['thumbnail'] = ThumbnailSerializer(thumbnail).data
        theme_s['category'] = CategorySerializer(category).data
        theme_s['topic'] = TopicSerializer(topic).data
        theme_s['browser'] = browser_s
        theme_s['screenshot'] = screenshot_s
        theme_s['label'] = label_s
        theme_s['review'] = review_s

        return Response(theme_s, status=200)        
