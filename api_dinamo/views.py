from rest_framework import viewsets, generics

from employees.models import EmployeeArticle
from main.models import Partner, Document
from photo_video.models import PhotoCategory
from vacancies.models import Vacancy
from .serializers import ServiceSerializer, CategoryServiceSerializer, NewsSerializer, EmployeeArticleSerializer, \
    PartnerSerializer, DocumentSerializer, VacancySerializer, NewsAllSerializer, PhotoCategorySerializer
from services.models import Service, CategoryService
from news.models import News


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Service model """
    queryset = Service.objects.filter(published=True)
    serializer_class = ServiceSerializer


class CategoryServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for CategoryService model """
    queryset = CategoryService.objects.all()
    serializer_class = CategoryServiceSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for News model (main page)"""
    queryset = News.objects.filter(published=True)
    serializer_class = NewsSerializer


class NewsAllViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for News model (for page with all news)"""
    queryset = News.objects.filter(published=True)
    serializer_class = NewsAllSerializer


class EmployeeArticleViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for EmployeeArticle model """
    queryset = EmployeeArticle.objects.filter(published=True)
    serializer_class = EmployeeArticleSerializer


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Partner model """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class DocumentViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Document model """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Vacancy model """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class PhotosViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for PhotoCategory model """
    queryset = PhotoCategory.objects.all()
    serializer_class = PhotoCategorySerializer