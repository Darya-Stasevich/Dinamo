from rest_framework import serializers

from services.models import Service, CategoryService


class CategoryServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для категории услуг"""
    class Meta:
        model = CategoryService
        fields = ('id', 'slug', 'title')


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для услуги"""
    class Meta:
        model = Service
        fields = ('id', 'slug', 'category', 'title', 'image', 'brief_description', 'description', 'price_with_VAT',
                  'price_without_VAT', 'notes', 'image', 'published')
