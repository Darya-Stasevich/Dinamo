from django.shortcuts import render

from employees.models import Management
from main.forms import UserEmailForm
from main.models import Contact, SocialNetwork, Partner, Video
from services.models import CategoryService


def index(request):
    """Отображение главной страницы сайта"""
    contact = Contact.objects.all()
    urls = SocialNetwork.objects.all()
    video = Video.objects.all()
    context = {
        'contact': contact,
        'urls': urls,
        'video': video,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, "index.html", context)


def about_stadium(request):
    """Отображение страницы сайта о стадионе"""
    contact = Contact.objects.all()
    urls = SocialNetwork.objects.all()
    context = {
        'contact': contact,
        'urls': urls,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, 'about_stadium.html', context)


def show_history(request):
    """Отображение страницы сайта о стадионе"""
    contact = Contact.objects.all()
    urls = SocialNetwork.objects.all()
    context = {
        'contact': contact,
        'urls': urls,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, 'history.html', context)


def show_management(request):
    """Отображение страницы сайта о руководстве"""
    contact = Contact.objects.all()
    urls = SocialNetwork.objects.all()
    managers = Management.objects.all()
    context = {
        'contact': contact,
        'urls': urls,
        'managers': managers,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, 'management.html', context)