from django.shortcuts import render

from employees.models import Management
from main.forms import UserEmailForm
from main.models import Contact, SocialNetwork


def show_management(request):
    """Отображение страницы сайта о руководстве"""
    contact = Contact.objects.last()
    url = SocialNetwork.objects.last()
    managers = Management.objects.all()
    context = {
        'contact': contact,
        'url': url,
        'managers': managers,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, 'management.html', context)


def show_employee_articles(request):
    """Отображение страницы сайта со статьями о сотрудниках"""
    contact = Contact.objects.last()
    url = SocialNetwork.objects.last()
    context = {
        'contact': contact,
        'url': url,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, 'employee_articles.html', context)