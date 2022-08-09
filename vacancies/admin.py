from django.contrib import admin
from vacancies.models import Vacancy, VacancyRequirements, MainInformationOfVacancy


class MainInformationOfVacancyInline(admin.StackedInline):
    model = MainInformationOfVacancy
    verbose_name_plural = 'Главная информация'
    verbose_name = 'Главная информация'


class VacancyRequirementsInline(admin.StackedInline):
    model = VacancyRequirements
    verbose_name_plural = 'Требования'
    verbose_name = 'Требование'


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title_of_vacancy', )
    inlines = ( MainInformationOfVacancyInline, VacancyRequirementsInline, )


admin.site.register(Vacancy, VacancyAdmin)
