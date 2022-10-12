from django.contrib import admin

from services.models import *


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title', 'category', 'published', 'is_primary_service', 'price_with_VAT_for_person', 'price_with_VAT_for_legal',
        'updated')
    list_filter = ('category', 'published', 'updated', 'is_primary_service')
    list_editable = ('published', 'is_primary_service')
    search_fields = ('title',)


class CategoryServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'status', 'date')
    list_filter = ('status', 'date')
    list_editable = ('status',)
    search_fields = ('name', 'phone_number')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Attachment)
admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Feedback, FeedbackAdmin)
