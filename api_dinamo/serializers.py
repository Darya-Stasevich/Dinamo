from rest_framework import serializers

from employees.models import EmployeeArticle
from main.models import Partner
from news.models import News
from services.models import Service, CategoryService


class CategoryServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для категории услуг"""

    class Meta:
        model = CategoryService
        fields = ['id', 'slug', 'title', ]


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения услуг на ГЛАВНОЙ странице"""

    class Meta:
        model = Service
        fields = ['id', 'slug', 'title', 'image', 'is_primary_service']


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения новостей на ГЛАВНОЙ странице"""

    class Meta:
        model = News
        fields = ['id', 'slug', 'title', 'brief_description', 'cover_image', ]


class EmployeeArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения статей про сотрудников на странице НАШИ СОТРУДНИКИ"""

    class Meta:
        model = EmployeeArticle
        fields = ['id', 'slug', 'name_employee', 'title', 'created', 'cover_image', ]


class PartnerSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения логотипов партнеров на главной странице"""

    class Meta:
        model = Partner
        fields = ['id', 'image', ]