"""dinamo_stadium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_dinamo import views
from main.views import index, about_stadium
from services.views import show_services_by_category, show_services_all

router = routers.DefaultRouter()
router.register('services', views.ServiceViewSet)
router.register('category_services', views.CategoryServiceViewSet)
router.register('news', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about_stadium/', about_stadium, name='about_stadium'),
    path('services/', show_services_all, name='show_services_all'),
    path('services/<slug:category_slug>/', show_services_by_category, name='show_services_by_category'),
    # path('service_detail/<slug:service_slug>/', service_detail, name='service_detail'),
    path('api_dinamo/', include(router.urls))


    # path('api/news_first_page',),   # endpoint для новостей на первой странице
    # path('api/news/<slug:news_slug><int:news_id>',),  # endpoint для перехода на страницу конретной новости
    # path('api/services_first_page',),    # endpoint для услуг на первой странице
    # path('api/services/<slug:category_slug><slug:service_slug><int:service_id>',),   # endpoint для перехода на страницу конкретной услуги

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
