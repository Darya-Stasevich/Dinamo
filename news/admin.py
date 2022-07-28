from django.contrib import admin

from news.models import NewsAdditionalImage, News


class NewsAdditionalImageInline(admin.TabularInline):
    """Класс для добавления в админке поля с дополнительными изображениями к модели News"""
    model = NewsAdditionalImage


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'brief_description', 'published', 'views', 'created', 'updated')
    list_editable = ('published',)
    list_filter = ('views', 'published', 'created')
    search_fields = ('title',)
    inlines = (NewsAdditionalImageInline,)


admin.site.register(News, NewsAdmin)