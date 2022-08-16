from django.db import models


class Vacancy(models.Model):
    title_of_vacancy = models.CharField(max_length=100, verbose_name='Название вакансии', unique=True)
    description = models.TextField(verbose_name='Описание вакансии')

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'

    def __str__(self):
        return f'{self.title_of_vacancy}'


class MainInformationOfVacancy(models.Model):
    title = models.CharField(max_length=100, verbose_name='Информация о вакансии',
                             help_text='Например, З/П до 1000 руб., Требуемый опыт работы, Полная занятость и т.п.')
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, verbose_name='Вакансия')


class VacancyRequirements(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название требования',
                             help_text='Например, ТРЕБОВАНИЯ, ОБЯЗАННОСТИ, ПРИВЕТСТВУЕТСЯ, ОПЫТ РАБОТЫ и т.д.')
    list_of_requirements = models.TextField(
        help_text=('Скопируйте этот тег в Пункты требования: &lt;li&gt;ВВЕДИТЕ ВАШ ТЕКСТ В ЭТОМ ТЕГЕ&lt;/li&gt;'),
        verbose_name='Пункты требования')
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, verbose_name='Вакансия')
