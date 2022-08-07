from django.shortcuts import render

from main.forms import UserEmailForm
from main.models import Contact, SocialNetwork, Partner, Video
from services.models import CategoryService


def index(request):
    """Отображение главной страницы сайта"""
    contact = Contact.objects.all()
    urls = SocialNetwork.objects.all()
    partners = Partner.objects.all()
    categories = CategoryService.objects.all()
    video = Video.objects.all()
    context = {
        'contact': contact,
        'urls': urls,
        'partners': partners,
        'categories': categories,
        'video': video,
    }
    print(video)
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

