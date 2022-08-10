from django.shortcuts import render

from services.models import Service


def show_services_all(request):
    """Функция вывода всех услуг организации"""
    services_all = Service.objects.filter(published=True).prefetch_related('category')
    context = {
        'services_all': services_all,
    }
    return render(request, 'services_by_category.html', context)


def show_services_by_category(request, category_slug):
    """Функция вывода всех услуг выбранной категории"""
    services = Service.objects.filter(published=True, category__slug=category_slug).prefetch_related('category')
    context = {
        'services': services,
    }
    return render(request, 'services_by_category.html', context)

