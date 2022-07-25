from django.db import models


class Management(models.Model):
    """Руководство организации"""
    position = models.CharField(max_length=200, verbose_name="Должность")
    name = models.CharField(max_length=200, verbose_name="ФИО")
    description = models.TextField(verbose_name="Биография")
    phone_number = models.CharField('Номер телефона', max_length=30, blank=True)
    email = models.EmailField(blank=True, verbose_name='Электронная почта')
    email_for_citizens = models.EmailField(blank=True, verbose_name='Электронная почта для обращений граждан')
    image = models.ImageField(upload_to='management/', verbose_name="Изображение",
                              blank=True)
    info_visits = models.CharField(max_length=200, verbose_name="Информация о времени приема граждан")

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

    def __str__(self):
        return self.name


class Worker(models.Model):
    pass


class Vacancy(models.Model):
    pass