from rest_framework import viewsets

from employees.models import EmployeeArticle
from main.models import Partner, Document
from vacancies.models import Vacancy
from .serializers import ServiceSerializer, CategoryServiceSerializer, NewsSerializer, EmployeeArticleSerializer, \
    PartnerSerializer, DocumentSerializer, VacancySerializer
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
    """ API for News model """
    queryset = News.objects.filter(published=True)
    serializer_class = NewsSerializer


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
