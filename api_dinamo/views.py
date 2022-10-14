from rest_framework import viewsets, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from employees.models import Management, Article
from history.models import HistoryArticle
from main.models import Partner, Document, SocialNetwork, Contact, UserEmail, DepartmentContacts, PaymentInfo, Managers
from photo_video.models import PhotoCategory, VideoCategory, PhotoLibrary
from vacancies.models import Vacancy, FeedbackForVacancy
from .serializers import ServiceSerializer, CategoryServiceSerializer, NewsSerializer, \
    PartnerSerializer, DocumentSerializer, VacancySerializer, NewsAllSerializer, PhotoCategorySerializer, \
    VideoCategorySerializer, SocialNetworkSerializer, ContactSerializer, UserEmailSerializer, ManagementSerializer, \
    HistoryArticleSerializer, DepartmentContactsSerializer, PaymentInfoSerializer, EventSerializer, \
    FeedbackForVacancySerializer, FeedbackSerializer, ServicesAllSerializer, ServiceDetailSerializer, \
    MarketingManagersSerializer, NewsDetailSerializer, PhotoLibrarySerializer, PhotoCategoryDetailSerializer, \
    VideoCategoryDetailSerializer, EmployeeArticleSerializer, EmployeeArticleDetailSerializer, ByCategorySerializer
from services.models import Service, CategoryService, Feedback
from news.models import News, Event


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Service model """
    queryset = Service.objects.filter(published=True)
    serializer_class = ServiceSerializer


class ServicesViewSetPagination(PageNumberPagination):
    """Пагинация для страницы все услуги"""
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100


class ServicesAllViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Service model (all services page)"""
    queryset = Service.objects.filter(published=True)
    serializer_class = ServicesAllSerializer
    pagination_class = ServicesViewSetPagination


class ServicesByCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Service model (all services page)"""
    queryset = CategoryService.objects.all()
    serializer_class = ByCategorySerializer
#
#     def retrieve(self, request, *args, **kwargs):
#         print(request)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)


class ServiceDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Service model detailed"""
    queryset = Service.objects.filter(published=True)
    serializer_class = ServiceDetailSerializer


class RandomServicesViewSet(viewsets.ReadOnlyModelViewSet):
    """API for 4 random services"""
    queryset = Service.objects.order_by('?')[:4]
    serializer_class = ServicesAllSerializer


class CategoryServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for CategoryService model """
    queryset = CategoryService.objects.all()
    serializer_class = CategoryServiceSerializer


class ContactViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    """ API for Contact model"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)


class DepartmentContactsViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    """ API for DepartmentContacts model"""
    queryset = DepartmentContacts.objects.all()
    serializer_class = DepartmentContactsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)


class MarketingMnagersViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    """ API for Managers model"""
    queryset = Managers.objects.all()
    serializer_class = MarketingManagersSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)


class PaymentInfoViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    """ API for PaymentInfo model"""
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)


class UserEmailViewSet(mixins.CreateModelMixin, GenericViewSet):
    """ API for UserEmail model"""
    queryset = UserEmail.objects.all()
    serializer_class = UserEmailSerializer


class SocialNetworkViewSet(mixins.ListModelMixin,
                           GenericViewSet):
    """ API for SocialNetwork model"""
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)


class EmployeeArticleViewSetPagination(PageNumberPagination):
    """Пагинация для страниц НАШИ СОТРУДНИКИ, НОВОСТИ"""
    page_size = 16
    page_size_query_param = 'page_size'
    max_page_size = 100


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for News model (main page)"""
    queryset = News.objects.filter(published=True)
    serializer_class = NewsSerializer


class NewsAllViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for News model (for page with all news)"""
    queryset = News.objects.filter(published=True)
    serializer_class = NewsAllSerializer
    pagination_class = EmployeeArticleViewSetPagination


class NewsDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for News model (for separate page)"""
    queryset = News.objects.filter(published=True)
    serializer_class = NewsDetailSerializer


class EmployeeArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Article model """
    queryset = Article.objects.filter(published=True)
    serializer_class = EmployeeArticleSerializer
    pagination_class = EmployeeArticleViewSetPagination


class EmployeeArticleDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for separate article about Employee """
    queryset = Article.objects.filter(published=True)
    serializer_class = EmployeeArticleDetailSerializer


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Partner model """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Document model """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class ManagementViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Document model """
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class HistoryArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for HistoryArticle model """
    queryset = HistoryArticle.objects.all()
    serializer_class = HistoryArticleSerializer


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Vacancy model """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class FeedbackForVacancyViewSet(mixins.CreateModelMixin, GenericViewSet):
    """ API for FeedbackForVacancy model """
    queryset = FeedbackForVacancy.objects.all()
    serializer_class = FeedbackForVacancySerializer


class FeedbackViewSet(mixins.CreateModelMixin, GenericViewSet):
    """ API for Feedback model """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for PhotoCategory model """
    queryset = PhotoCategory.objects.all()
    serializer_class = PhotoCategorySerializer


class PhotoDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for separate PhotoLibrary """
    queryset = PhotoCategory.objects.all()
    serializer_class = PhotoCategoryDetailSerializer


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for PhotoCategory model """
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer


class VideoDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for separate VideoLibrary """
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategoryDetailSerializer


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Event model """
    queryset = Event.objects.filter(published=True)
    serializer_class = EventSerializer
