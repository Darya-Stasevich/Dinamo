from rest_framework import viewsets

from employees.models import EmployeeArticle
from main.models import Partner
from .serializers import ServiceSerializer, CategoryServiceSerializer, NewsSerializer, EmployeeArticleSerializer, \
    PartnerSerializer
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