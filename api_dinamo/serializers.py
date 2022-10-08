from rest_framework import serializers

from employees.models import EmployeeArticle
from main.models import Partner, Document, SocialNetwork, Contact, UserEmail
from news.models import News
from photo_video.models import PhotoLibrary, PhotoCategory, VideoLibrary, VideoCategory
from services.models import Service, CategoryService
from vacancies.models import Vacancy, VacancyRequirements


class CategoryServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для категории услуг"""

    class Meta:
        model = CategoryService
        fields = ['id', 'slug', 'title', ]


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор для контактов в футер"""

    class Meta:
        model = Contact
        fields = ['number_phone_main', 'email_main', ]

class UserEmailSerializer(serializers.ModelSerializer):
    """Сериализатор для формы email в футер"""

    class Meta:
        model = UserEmail
        fields = ['email',]


class SocialNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для социальных сетей"""

    class Meta:
        model = SocialNetwork
        fields = ['social_TG', 'social_Youtube', 'social_Facebook', 'social_Instagram', 'social_VK']


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


class NewsAllSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения новостей на странице со всеми новостями"""

    class Meta:
        model = News
        fields = ['id', 'slug', 'cover_image', 'title', 'created', 'time_for_reading', ]


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
        fields = ['id', 'title', 'list_of_requirements', ]


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения вакансий"""
    vacancyrequirements_set = VacancyRequirementsSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = ['id', 'title_of_vacancy', 'salary', 'experience', 'employment', 'vacancyrequirements_set', ]


class PhotoLibrarySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения фотографий конкретного альбома"""

    class Meta:
        model = PhotoLibrary
        fields = ['id', 'image', ]


class PhotoCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения альбомов с фотографиями"""
    photos = PhotoLibrarySerializer(many=True)

    class Meta:
        model = PhotoCategory
        fields = ['id', 'slug', 'title', 'cover', 'photos', ]


class VideoLibrarySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения видео конкретного альбома"""

    class Meta:
        model = VideoLibrary
        fields = ['id', 'path', ]


class VideoCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для отображения альбомов с видео"""
    videos = VideoLibrarySerializer(many=True)

    class Meta:
        model = VideoCategory
        fields = ['id', 'slug', 'title', 'cover', 'videos', ]
