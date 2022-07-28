from django.db import models
from django.urls import reverse


class News(models.Model):
    """Новости организации"""
    title = models.CharField(max_length=200, unique=True, verbose_name="Заголовок новости")
    slug = models.SlugField(unique=True)
    brief_description = models.CharField(max_length=400, verbose_name="Краткое содержание новости")
    description = models.TextField(verbose_name="Полное содержание новости")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания новости")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования новости")
    cover_image = models.ImageField(upload_to='news/', verbose_name="Заглавная картинка для новости")
    time_for_reading = models.IntegerField(verbose_name='Время прочтения новости')
    video_url = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ссылка на видео к новости")
    views = models.IntegerField(default=0, blank=True, null=True, verbose_name="Количество просмотров")
    published = models.BooleanField('Опубликовать на сайте', default=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f'{self.title}, дата создания: {self.created}'

    # def get_absolute_url(self):
    #     return reverse('news:news_detail', args=[self.id])


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


# class Event(models.Model):
#     pass