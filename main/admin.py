from django.contrib import admin

from main.models import *


class VideoAdditionalInline(admin.TabularInline):
    """Класс для добавления в админке поля с дополнительными ссылками на видео для главнлой страницы"""
    model = VideoAdditional


class VideoAdmin(admin.ModelAdmin):
    inlines = (VideoAdditionalInline,)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Contact)
admin.site.register(SocialNetwork)
admin.site.register(Video, VideoAdmin)
admin.site.register(PaymentInfo)
admin.site.register(Partner)
admin.site.register(UserEmail)
admin.site.register(Document, DocumentAdmin)