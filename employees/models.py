from django.db import models


class Management(models.Model):
    """Руководство организации"""
    name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=200, verbose_name="Должность")
    image = models.ImageField(upload_to='management/', verbose_name="Фотография")
    description_1 = models.TextField(verbose_name="Биография, абзац 1")
    description_2 = models.TextField(blank=True, null=True, verbose_name="Биография, абзац 2")
    description_3 = models.TextField(blank=True, null=True, verbose_name="Биография, абзац 3")
    description_4 = models.TextField(blank=True, null=True, verbose_name="Биография, абзац 4")
    phone_number = models.CharField(max_length=30, verbose_name='Номер телефона для связи')
    email = models.EmailField(verbose_name='Электронная почта сотрудника')
    email_for_citizens = models.EmailField(blank=True, null=True,
                                           verbose_name='Электронная почта для обращений граждан')
    info_visits = models.CharField(blank=True, null=True, max_length=200,
                                   verbose_name="Информация о времени приема граждан",
                                   help_text='Пример заполнения: каждый четверг с 18.00 до 20.00')

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

    def __str__(self):
        return self.name


class Article(models.Model):
    """Статья о сотруднике организации"""
    name_employee = models.CharField(max_length=200, verbose_name="Фамилия, имя")
    title = models.CharField(max_length=150, verbose_name='Название статьи',)
    slug = models.SlugField(unique=True)
    cover_image = models.ImageField(upload_to='employees/',
                                    verbose_name="Главная картинка для статьи про сотрудника")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания статьи")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования статьи")
    published = models.BooleanField('Опубликовать на сайте', default=True)

    class Meta:
        verbose_name = 'Статью о сотруднике'
        verbose_name_plural = 'Статьи о сотрудниках'

    def __str__(self):
        return f'{self.name_employee}, {self.title}'


class ArticleBlock(models.Model):
    """Текст и картинки статьи"""
    text_1 = models.TextField(verbose_name="Абзац 1", )
    text_2 = models.TextField(blank=True, null=True, verbose_name="Абзац 2")
    text_3 = models.TextField(blank=True, null=True, verbose_name="Абзац 3")
    text_4 = models.TextField(blank=True, null=True, verbose_name="Абзац 4")
    image_1 = models.ImageField(upload_to='employees/', blank=True, null=True, verbose_name="Фотография 1")
    image_2 = models.ImageField(upload_to='employees/', blank=True, null=True, verbose_name="Фотография 2")
    image_3 = models.ImageField(upload_to='employees/', blank=True, null=True,  verbose_name="Фотография 3")
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='blocks')