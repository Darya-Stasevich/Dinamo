from rest_framework import serializers

from news.models import News
from services.models import Service, CategoryService


class CategoryServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для категории услуг"""
    class Meta:
        model = CategoryService
        fields = ('id', 'slug', 'title')


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения услуг на первой странице"""
    class Meta:
        model = Service
        fields = ('id', 'slug', 'title', 'image')


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения новостей на первой странице"""
    class Meta:
        model = News
        fields = ('id', 'slug', 'title', 'brief_description', 'cover_image')

