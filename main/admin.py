from django.contrib import admin

# from main.models import Contact, SocialNetwork, PaymentInfo, Partner, Service, CategoryService, UsersEmail, Order
from main.models import *

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Contact)
admin.site.register(SocialNetwork)
admin.site.register(PaymentInfo)
admin.site.register(Partner)
# admin.site.register(Service, ServiceAdmin)
# admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(UserEmail)
# admin.site.register(Order)