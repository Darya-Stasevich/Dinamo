from django.shortcuts import render

from main.forms import UserEmailForm
from main.models import Contact, SocialNetwork, Partner


def index(request):
    "Отображение главной страницы сайта"
    contact = Contact.objects.all()
    social = SocialNetwork.objects.all()
    partners = Partner.objects.all()
    context = {
        'contact': contact,
        'social': social,
        'partners': partners,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, "index.html", context)

