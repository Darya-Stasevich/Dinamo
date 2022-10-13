from django.contrib import admin

from employees.models import Management, ArticleBlock, Article


class ManagementAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone_number', 'email')
    list_editable = ('phone_number',)
    search_fields = ('name', 'position')


class ArticleBlocksInline(admin.StackedInline):
    model = ArticleBlock
    verbose_name_plural = 'Новый блок статьи'
    verbose_name = 'Новые блоки статьи'


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name_employee', 'title')}
    list_display = ('name_employee', 'title', 'published', 'created', 'updated')
    list_editable = ('published',)
    list_filter = ('published', 'created')
    search_fields = ('title', 'name_employee')
    inlines = (ArticleBlocksInline, )


admin.site.register(Management, ManagementAdmin)
admin.site.register(Article, ArticleAdmin)