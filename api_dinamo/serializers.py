from rest_framework import serializers

from employees.models import EmployeeArticle, Management
from history.models import HistoryArticle
from main.models import Partner, Document, SocialNetwork, Contact, UserEmail, DepartmentContacts, PaymentInfo, Managers
from news.models import News, Event
from photo_video.models import PhotoLibrary, PhotoCategory, VideoLibrary, VideoCategory
from services.models import Service, CategoryService, Feedback
from vacancies.models import Vacancy, VacancyRequirements, FeedbackForVacancy


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


class DepartmentContactsSerializer(serializers.ModelSerializer):
    """Сериализатор для контактов на странице контакты"""

    class Meta:
        model = DepartmentContacts
        exclude = ['id', ]


class MarketingManagersSerializer(serializers.ModelSerializer):
    """Сериализатор для контактов сотрудников отдела маркетинга"""

    class Meta:
        model = Managers
        exclude = ['id', ]


class PaymentInfoSerializer(serializers.ModelSerializer):
    """Сериализатор для реквизитов оплаты"""

    class Meta:
        model = PaymentInfo
        exclude = ['id', ]


class UserEmailSerializer(serializers.ModelSerializer):
    """Сериализатор для формы email в футер"""

    class Meta:
        model = UserEmail
        fields = ['email', ]


class SocialNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для социальных сетей"""

    class Meta:
        model = SocialNetwork
        fields = ['social_TG', 'social_Youtube', 'social_Facebook', 'social_Instagram', 'social_VK', ]


class ManagementSerializer(serializers.ModelSerializer):
    """Сериализатор для руководства"""

    class Meta:
        model = Management
        fields = '__all__'


class HistoryArticleSerializer(serializers.ModelSerializer):
    """Сериализатор для ссылок на исторические статьи"""

    class Meta:
        model = HistoryArticle
        fields = ['id', 'title', 'url', ]


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения услуг на ГЛАВНОЙ странице"""

    class Meta:
        model = Service
        fields = ['id', 'slug', 'title', 'image', 'is_primary_service', ]


class ServicesAllSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения услуг на странице ВСЕХ УСЛУГ"""

    class Meta:
        model = Service
        fields = ['id', 'slug', 'category', 'title', 'image', 'brief_description', 'price_with_VAT_for_person', ]


class ServiceDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения данных об услуге"""

    class Meta:
        model = Service
        exclude = ["published", "created", "updated", "is_primary_service", 'category', 'brief_description', 'image', ]
        depth = 1


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
    requirements = VacancyRequirementsSerializer(many=True)

    class Meta:
        model = Vacancy
        fields = ['id', 'title_of_vacancy', 'salary', 'experience', 'employment', 'requirements', ]


class FeedbackForVacancySerializer(serializers.ModelSerializer):
    """Сериализатор для формы заявка на вакансию"""

    class Meta:
        model = FeedbackForVacancy
        fields = ['full_name', 'phone_number', 'resume_file', 'url_of_resume', 'vacancy', ]


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализатор для формы заявка перезвонить"""

    class Meta:
        model = Feedback
        fields = ['name', 'phone_number', ]


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


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для событий"""

    class Meta:
        model = Event
        fields = ['id', 'brief_description', 'date', 'image', ]