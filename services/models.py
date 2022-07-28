from django.db import models
from django.urls import reverse


class CategoryService(models.Model):
    """Классификация услуг"""
    CHOICES_CATEGORY = (
        ('Футбольное поле', 'Футбольное поле'),
        ('Реклама', 'Реклама'),
        ('Спорт', 'Спорт'),
        ('Здоровье', 'Здоровье'),
        ('Организация мероприятий', 'Организация мероприятий'),
        ('Прочие услуги', 'Прочие услуги'),
    )
    title = models.CharField('Категория услуги', max_length=40, choices=CHOICES_CATEGORY)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категорию услуг'
        verbose_name_plural = 'Категории услуг'

    def __str__(self):
        return self.title


class Service(models.Model):
    """Услуги организации"""
    category = models.ForeignKey(
        'CategoryService',
        on_delete=models.PROTECT,
        verbose_name="Категория услуги"
    )
    title = models.CharField(max_length=200, verbose_name="Название услуги")
    slug = models.SlugField(unique=True)
    brief_description = models.CharField(max_length=400, verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Полное описание")
    price_with_VAT = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Тариф с НДС", default=0)
    price_without_VAT = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Тариф без НДС", default=0)
    notes = models.CharField(max_length=200, verbose_name="Ед.измерения", blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Изображение")
    published = models.BooleanField('Добавить на сайт', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления услуги")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования услуги")

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('main:service_detail', args=[self.slug])


class Feedback(models.Model):
    """Заявка перезвонить от клиента"""
    CHOICES_STATUS = (
        ('в обработке', 'в обработке'),
        ('новая заявка', 'новая заявка'),
        ('обработана', 'обработана'),
    )
    name = models.CharField(max_length=60, verbose_name="Имя клиента")
    phone_number = models.CharField('Номер телефона', max_length=30)
    status = models.CharField('Статус заявки', max_length=20, choices=CHOICES_STATUS, default='новая заявка')
    date = models.DateTimeField('Дата и время заявки', auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Заявку'
        verbose_name_plural = 'ЗАЯВКИ ПЕРЕЗВОНИТЬ'

    def __str__(self):
        return f'{self.name},{self.phone_number}'
