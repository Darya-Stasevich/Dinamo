from django.db import models
from django.urls import reverse


class News(models.Model):
    """Новости организации"""
    image = models.ImageField(upload_to='news/', verbose_name="Изображение")
    published = models.BooleanField('Опубликовать на сайте', default=True)
    title = models.CharField(max_length=200, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Содержание")
    brief_description = models.CharField(max_length=400, verbose_name="Краткое содержание")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    # views = models.IntegerField(default=0, blank=True, verbose_name="Просмотры")
    # slug

    class Meta:
        ordering = ['created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.id])


class NewsAdditionalImage(models.Model):
    """Дополнительные изображения к новостям"""
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость'
    )
    image = models.ImageField(upload_to='news/', blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Дополнительное изображение'
        verbose_name_plural = 'Дополнительные изображения'


class Event(models.Model):
    pass