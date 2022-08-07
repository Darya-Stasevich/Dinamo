from rest_framework import viewsets
from .serializers import ServiceSerializer, CategoryServiceSerializer, NewsSerializer
from services.models import Service, CategoryService
from news.models import News


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for Service model """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class CategoryServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for CategoryService model """
    queryset = CategoryService.objects.all()
    serializer_class = CategoryServiceSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    """ API for News model """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
