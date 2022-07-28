from django.db import models


class Management(models.Model):
    """Руководство организации"""
    position = models.CharField(max_length=200, verbose_name="Должность")
    name = models.CharField(max_length=200, verbose_name="ФИО")
    description = models.TextField(verbose_name="Биография", blank=True, null=True)
    phone_number = models.CharField('Номер телефона для связи', max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, verbose_name='Электронная почта сотрудника')
    email_for_citizens = models.EmailField(blank=True, null=True,
                                           verbose_name='Электронная почта для обращений граждан')
    image = models.ImageField(upload_to='management/', verbose_name="Фотография",
                              blank=True, null=True)
    info_visits = models.CharField(max_length=200, verbose_name="Информация о времени приема граждан")

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

    def __str__(self):
        return self.name


class EmployeeArticle(models.Model):
    """Статья о сотруднике организации"""
    name_employee = models.CharField(max_length=200, verbose_name="ФИО")
    slug = models.SlugField(unique=True)
    title = models.CharField('Название статьи', max_length=150, blank=True, null=True)
    description = models.TextField(verbose_name="Биография", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания статьи")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования статьи")
    published = models.BooleanField('Опубликовать на сайте', default=True)
    cover_image = models.ImageField(upload_to='employees/', verbose_name="Главная картинка для статьи про сотрудника",
                                    blank=True, null=True)

    class Meta:
        verbose_name = 'Статью о сотруднике'
        verbose_name_plural = 'Статьи о сотрудниках'

    def __str__(self):
        return f'{self.name_employee}, {self.title}'


class ArticleAdditionalImage(models.Model):
    """Дополнительные изображения к статье о сотруднике"""
    article = models.ForeignKey(
        EmployeeArticle,
        on_delete=models.CASCADE,
        verbose_name='Статья о сотруднике'
    )
    image = models.ImageField(upload_to='employees/', blank=True, null=True,
                              verbose_name='Картинка для статьи о сотруднике')

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'


# class Vacancy(models.Model):
#     pass
