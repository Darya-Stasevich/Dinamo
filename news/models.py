from django.db import models
from django.urls import reverse


class News(models.Model):
    """Новости организации"""
    title = models.CharField(max_length=200, unique=True, verbose_name="Заголовок новости")
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to='news/', verbose_name="Заглавная картинка для новости")
    brief_description = models.CharField(max_length=500, verbose_name="Краткое содержание новости")
    description_1 = models.TextField(verbose_name="Полное содержание новости, 1 абзац")
    description_2 = models.TextField(verbose_name="Полное содержание новости, 2 абзац", blank=True, null=True)
    description_3 = models.TextField(verbose_name="Полное содержание новости, 3 абзац", blank=True, null=True)
    time_for_reading = models.IntegerField(verbose_name='Время прочтения новости')
    text_source = models.CharField(max_length=50, verbose_name="Источник новости", blank=True, null=True,
                                   help_text='Пример заполнения: Источник: sport.tut.by')
    picture_source = models.CharField(max_length=50, verbose_name="Источник фотографий", blank=True, null=True,
                                      help_text='Пример заполнения: Фото: ФК "Динамо-Минск"')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания новости")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования новости")
    video_url = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ссылка на видео к новости")
    views = models.IntegerField(default=0, blank=True, null=True, verbose_name="Количество просмотров")
    published = models.BooleanField('Опубликовать на сайте', default=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title}, дата создания: {self.created}'


class NewsAdditionalImage(models.Model):
    """Дополнительные изображения к новостям"""
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость'
    )
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name='Картинка для новости')

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'


class Event(models.Model):
    """Страница событий/мероприятий"""

    brief_description = models.CharField(max_length=400, verbose_name="Краткое описание события")
    date = models.CharField(max_length=200, verbose_name="Дата проведения",
                            help_text='Пример заполнения: 18 августа - 20 августа 2022')
    image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name='Картинка для события')
    published = models.BooleanField('Опубликовать на сайте', default=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.brief_description}, дата проведения: {self.date}'
