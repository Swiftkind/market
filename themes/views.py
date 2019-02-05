from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from .models import (Theme, Thumbnail, Screenshot, Review, Browser, Category, Topic, Label, License)
from .serializers import (ThemeDetailSerializer, ThumbnailSerializer, CategorySerializer, TopicSerializer, LicenseSerializer)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from itertools import chain 
import json


class ThemeFeed(APIView):
    """themes home
    """
    queryset = Theme.objects.all()
    permission_classes = (AllowAny,)

    def get(self,*args,**kwargs):
        thumbnail = Thumbnail.objects.all().values()
        category = Category.objects.all().values()

        data = self.queryset.filter(
            id__in=thumbnail.values('theme_id')
        ).values('id','name','rating','price','thumbnail__thumbnail','category__category')

        return Response({
            'data': list(data),
            'category': list(category),
        }, status=200)


class ThemeNameFilter(APIView):
    """themes details
    """
    permission_classes = (AllowAny,)

    def get(self,*args,**kwargs):
        theme = Theme.objects.get(id=kwargs['id'])
        review = Review.objects.filter(theme_id=theme.id
                ).values('rating','comment','date_created','user__first_name','user__last_name')
        
        screenshot = Screenshot.objects.filter(theme_id=theme.id).values('image')
        browser = theme.browser.all().values('browser')
        label = theme.labels.all().values('label')
        thumbnail = Thumbnail.objects.get(theme_id=theme.id)
        category = Category.objects.get(id=theme.category_id)
        topic = Topic.objects.get(id=theme.topic_id)
        
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


class ThemeCart(APIView):
    """theme cart
    """
    permission_classes = (AllowAny,)

    def get(self,*args,**kwargs):
        theme = Theme.objects.get(id=kwargs['id'])
        category = Category.objects.get(id=theme.category_id)
        thumbnail = Thumbnail.objects.get(theme_id=theme.id)
        license = License.objects.get(id=theme.license_id)

        theme_s = ThemeDetailSerializer(theme).data
        theme_s['thumbnail'] = ThumbnailSerializer(thumbnail).data
        theme_s['category'] = CategorySerializer(category).data
        theme_s['license'] = LicenseSerializer(license).data
        
        return Response(theme_s, status=200)


class CategoryView(APIView):
    """category 
    """
    permission_classes = (AllowAny,)

    def get(self,*args,**kwargs):
        category = Category.objects.all().values('category')

        return Response({'category': list(category)}, status=200)
