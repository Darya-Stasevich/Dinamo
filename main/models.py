from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Классификация услуг"""
    title = models.CharField(max_length=50, verbose_name="Категория услуги")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Contact(models.Model):
    """Контакты организации"""
    address = models.CharField('Адрес', max_length=250, help_text='Можно использовать тег %br> для переноса текста')
    number_phone = models.CharField('Номер телефона', max_length=30)
    email = models.EmailField(blank=False, verbose_name='Электронная почта организации')
    social_TG = models.CharField('Социальная сеть Телеграмм', max_length=250, blank=True, null=True)
    social_Youtube = models.CharField('Социальная сеть YouTube', max_length=250, blank=True, null=True)
    social_Facebook = models.CharField('Социальная сеть Фейсбук', max_length=250, blank=True, null=True)
    social_Instagram = models.CharField('Социальная сеть Инстаграм', max_length=250, blank=True, null=True)
    social_VK = models.CharField('Социальная сеть ВКонтакте', max_length=250, blank=True, null=True)


    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.address


class Partner(models.Model):
    image = models.ImageField(upload_to='partners/', verbose_name="Изображение", blank=True)


class SubService(models.Model):
    """Разбивка услуги на подуслуги"""
    service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Подуслуга")
    title = models.CharField(max_length=200, unique=True, verbose_name="Название подуслуги")
    price_with_VTA = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name="Тариф с НДС")
    price_without_VTA = models.DecimalField(max_digits=10, decimal_places=2,
                                            verbose_name="Тариф без НДС")

    class Meta:
        verbose_name = 'Подуслуга'
        verbose_name_plural = 'Подуслуги'

    def __str__(self):
        return self.title


class Service(models.Model):
    """Услуги организации"""
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Название услуги")
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name="Стоимость")     # если нужно написать от или индивидуально?
    description = models.TextField(verbose_name="Полное описание")
    brief_description = models.CharField(max_length=400, verbose_name="Краткое описание")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    image = models.ImageField(upload_to='services/', verbose_name="Изображение", blank=True)    # картинка к какжой услуге, а если нет?

    class Meta:
        ordering = ['created']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:service_detail', args=[self.id])


class News(models.Model):
    pass


class Event(models.Model):
    pass


class UsersEmail(models.Model):
    """Электронный адрес пользователя, который хочет получать уведомления о новостях"""
    email = models.EmailField(blank=False, verbose_name='Электронная почта клиента')

    class Meta:
        verbose_name = 'Адрес электронной почты'
        verbose_name_plural = 'Адреса электронной почты'

    def __str__(self):
        return self.email


class Order(models.Model):
    """Заявка перезвонить от клиента"""
    CHOICES_STATUS = (
        ('в обработке', 'в обработке'),
        ('новая заявка', 'новая заявка'),
        ('обработана', 'обработана'),
    )
    name = models.CharField(max_length=60,  verbose_name="Имя клиента")
    number_phone = models.CharField('Номер телефона', max_length=30)
    status = models.CharField('Статус заявки', max_length=20, choices=CHOICES_STATUS, default='новая заявка')


class Worker(models.Model):
    pass


class Management(models.Model):
    pass


class OpenPosition(models.Model):
    pass


class PhotoLibrary(models.Model):
    pass


class VideoLibrary(models.Model):
    pass