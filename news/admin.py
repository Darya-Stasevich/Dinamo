# from django.contrib import admin
#
# from news.models import NewsAdditionalImage, News
#
#
# class NewsAdditionalImageInline(admin.TabularInline):
#     """Класс для добавления в админке поля с дополнительными изображениями к модели Post"""
#     model = NewsAdditionalImage
#
#
# class NewsAdmin(admin.ModelAdmin):
#     """Отредактированный для админки класс News с возможностью прикреплять дополнительные изображения"""
#     fields = ('title', 'description', 'brief_description', 'image')
#     list_display = ('title', 'description', 'brief_description', 'created', 'updated', 'image')
#     inlines = (NewsAdditionalImageInline,)
#
#
# admin.site.register(News, NewsAdmin)