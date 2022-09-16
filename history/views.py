from django.shortcuts import render

from history.models import History, HistoryArticle
from main.forms import UserEmailForm
from main.models import Contact, SocialNetwork


def show_history(request):
    """Отображение страницы сайта об истории стадионе"""
    contact = Contact.objects.last()
    url = SocialNetwork.objects.last()
    numbers = History.objects.last()
    history_articles = HistoryArticle.objects.all()
    context = {
        'contact': contact,
        'url': url,
        'numbers': numbers,
        'history_articles': history_articles,
    }
    if request.method == "POST":
        email = UserEmailForm(request.POST)
        if email.is_valid():
            email.save()
    return render(request, 'history.html', context)
