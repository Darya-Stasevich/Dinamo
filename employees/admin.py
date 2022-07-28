from django.contrib import admin

from employees.models import ArticleAdditionalImage, EmployeeArticle, Management


class ArticleAdditionalImageInline(admin.TabularInline):
    """Класс для добавления в админке поля с дополнительными изображениями к модели News"""
    model = ArticleAdditionalImage


class EmployeeArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name_employee",)}
    list_display = ('name_employee', 'title', 'description', 'published', 'created', 'updated')
    list_editable = ('published',)
    list_filter = ('published', 'created')
    search_fields = ('title', 'name_employee')
    inlines = (ArticleAdditionalImageInline,)


class ManagementAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone_number', 'email')
    list_editable = ('phone_number',)
    search_fields = ('name', 'position')


admin.site.register(EmployeeArticle, EmployeeArticleAdmin)
admin.site.register(Management, ManagementAdmin)
