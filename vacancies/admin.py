from django.contrib import admin
from vacancies.models import Vacancy, VacancyRequirements, FeedbackForVacancy


class VacancyRequirementsInline(admin.StackedInline):
    model = VacancyRequirements
    verbose_name_plural = 'Требования'
    verbose_name = 'Требование'


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title_of_vacancy', 'published')
    list_editable = ('published', )
    inlines = (VacancyRequirementsInline, )


class FeedbackForVacancyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'status', 'date', 'vacancy')
    list_filter = ('status', 'date', 'vacancy')
    list_editable = ('status', )
    search_fields = ('full_name', 'phone_number')


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(FeedbackForVacancy, FeedbackForVacancyAdmin)