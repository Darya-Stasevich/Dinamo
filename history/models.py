from django.db import models


class History(models.Model):
    """Цифры о стадионе на странице истории"""
    age = models.IntegerField(verbose_name='Возраст стадиона')

    class Meta:
        verbose_name = 'Возраст стадиона'
        verbose_name_plural = 'Возраст стадиона'

    def __str__(self):
        return "Возарст стадиона на странице 'История стадиона'"


class HistoryArticle(models.Model):
    """Ссылки на статьи о стадионе"""
    title = models.CharField(max_length=150, verbose_name='Заголовок статьи')
    url = models.CharField(max_length=250, verbose_name='Ссылка на статью')

    class Meta:
        verbose_name = 'Ссылку на статью о стадионе'
        verbose_name_plural = 'Ссылки на статьи о стадионе'

    def __str__(self):
        return self.title
