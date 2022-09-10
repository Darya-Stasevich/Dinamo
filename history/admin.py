from django.contrib import admin

from history.models import History, HistoryArticle

admin.site.register(History)
admin.site.register(HistoryArticle)
