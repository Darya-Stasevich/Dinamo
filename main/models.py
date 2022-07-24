from django.db import models
from django.urls import reverse


class Contact(models.Model):
    """Контакты организации"""
    number_phone_main = models.CharField('Общий номер телефона', max_length=30, blank=False)
    email_main = models.EmailField(blank=False, verbose_name='Общая электронная почта организации')

    number_phone_reception = models.CharField('Номер приемной', max_length=30, blank=True)
    email_reception_1 = models.EmailField(blank=True, verbose_name='Электронная почта приемной №1')
    email_reception_2 = models.EmailField(blank=True, verbose_name='Электронная почта приемной №2')
    contact_person_reception = models.CharField(max_length=200, verbose_name="Контактное лицо приемная")

    number_phone_ad = models.CharField('Номер отдела рекламы', max_length=30, blank=True)
    email_ad = models.EmailField(blank=True, verbose_name='Электронная почта отдела рекламы')
    contact_person_ad = models.CharField(max_length=200, verbose_name="Контактное лицо отдел рекламы")

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class SocialNetwork(models.Model):
    social_TG = models.CharField('Социальная сеть Телеграмм', max_length=250, blank=True, null=True)
    social_Youtube = models.CharField('Социальная сеть YouTube', max_length=250, blank=True, null=True)
    social_Facebook = models.CharField('Социальная сеть Фейсбук', max_length=250, blank=True, null=True)
    social_Instagram = models.CharField('Социальная сеть Инстаграм', max_length=250, blank=True, null=True)
    social_VK = models.CharField('Социальная сеть ВКонтакте', max_length=250, blank=True, null=True)


    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = 'Соцсети'

class PaymentInfo(models.Model):
    account1 = models.CharField('Р/с бюджет', max_length=50, blank=True, null=True)
    account2 = models.CharField('Р/с внебюджет', max_length=50, blank=True, null=True)
    UNP = models.CharField('УНП', max_length=10, blank=True, null=True)
    OKPO = models.CharField('ОКПО', max_length=10, blank=True, null=True)
    bank_name = models.CharField('Наименование банка', max_length=50, blank=True, null=True)
    bank_address = models.CharField('Адрес банка', max_length=70, blank=True, null=True)
    bank_BIC = models.CharField('BIC банка', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'


class Partner(models.Model):
    """Партнеры организации"""
    image = models.ImageField(upload_to='partners_logo/', verbose_name="Изображение", blank=True)


class CategoryService(models.Model):
    """Классификация услуг"""
    title = models.CharField(max_length=50, verbose_name="Категория услуги")

    class Meta:
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'

    def __str__(self):
        return self.title


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
    phone_number = models.CharField('Номер телефона', max_length=30)
    status = models.CharField('Статус заявки', max_length=20, choices=CHOICES_STATUS, default='новая заявка')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.name},{self.phone_number}'


class News(models.Model):
    pass


class Event(models.Model):
    pass


class Worker(models.Model):
    pass


class Management(models.Model):
    """Руководство организации"""
    position = models.CharField(max_length=200, verbose_name="Должность")
    name = models.CharField(max_length=200, verbose_name="ФИО")
    description = models.TextField(verbose_name="Биография")
    phone_number = models.CharField('Номер телефона', max_length=30, blank=True)
    email = models.EmailField(blank=True, verbose_name='Электронная почта ')
    email_for_citizens = models.EmailField(blank=True, verbose_name='Электронная почта для обращений граждан')
    image = models.ImageField(upload_to='management/', verbose_name="Изображение",
                              blank=True)
    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

    def __str__(self):
        return self.name


class OpenPosition(models.Model):
    pass


class PhotoCategory(models.Model):
    """Раздел фотоальбома"""
    title = models.CharField(max_length=200, verbose_name="Рубрика фотографии")
    cover = models.ImageField(upload_to='photo_library/covers', verbose_name="Изображение", blank=True)

    class Meta:
        verbose_name = 'Раздел фотоальбома'
        verbose_name_plural = 'Разделы фотоальбома'

    def __str__(self):
        return self.title


class PhotoLibrary(models.Model):
    pass


class VideoCategory(models.Model):
    """Раздел видеоальбома"""
    title = models.CharField(max_length=200, unique=True, verbose_name="Рубрика видео")
    cover = models.ImageField(upload_to='video_library/covers', verbose_name="Обложки для видео", blank=True)

    class Meta:
        verbose_name = 'Раздел видеоальбома'
        verbose_name_plural = 'Разделы видеоальбома'

    def __str__(self):
        return self.title

class VideoLibrary(models.Model):
    pass