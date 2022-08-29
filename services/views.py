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
<<<<<<< HEAD
    services = Service.objects.filter(category__slug=category_slug)
=======
    print(request)
    services = Service.objects.filter(published=True, category__slug=category_slug).prefetch_related('category')
>>>>>>> 51ddcdc0d5d2d9d7ac6aea0358859e505720ca2b
    context = {
        'services_all': services,
    }
    return render(request, 'services_by_category.html', context)

