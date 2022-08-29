from rest_framework import serializers

from employees.models import EmployeeArticle
from main.models import Partner, Document
from news.models import News
from services.models import Service, CategoryService
from vacancies.models import Vacancy, VacancyRequirements


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


class DocumentSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения документов"""

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', ]

class VacancyRequirementsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения требований к вакансии"""

    class Meta:
        model = VacancyRequirements
        fields = ['id', 'title', 'list_of_requirements',  ]


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения вакансий"""
    vacancyrequirements_set = VacancyRequirementsSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = ['id', 'title_of_vacancy', 'salary', 'experience', 'employment', 'vacancyrequirements_set', ]



