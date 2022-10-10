from django.contrib import admin

from main.models import *


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Contact)
admin.site.register(DepartmentContacts)
admin.site.register(SocialNetwork)
admin.site.register(PaymentInfo)
admin.site.register(Partner)
admin.site.register(UserEmail)
admin.site.register(Document, DocumentAdmin)