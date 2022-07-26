from django.db import models
from django.urls import reverse


class Contact(models.Model):
    """Контакты организации"""
    number_phone_main = models.CharField('Общий номер телефона', max_length=30, blank=False)
    email_main = models.EmailField(blank=False, verbose_name='Общая электронная почта организации')

    number_phone_reception = models.CharField('Номер тел. приемной', max_length=30, blank=True, null=True)
    email_reception_1 = models.EmailField(blank=True, null=True, verbose_name='Электронная почта №1 приемная')
    email_reception_2 = models.EmailField(blank=True, null=True, verbose_name='Электронная почта №2 приемная')
    contact_person_reception = models.CharField(max_length=200, blank=True, null=True, verbose_name="Контактное лицо приемная")

    number_phone_ad = models.CharField('Номер тел. отдел рекламы', max_length=30, blank=True, null=True)
    email_ad = models.EmailField(blank=True, null=True, verbose_name='Электронная почта отдел рекламы')
    contact_person_ad = models.CharField(max_length=200, blank=True, null=True, verbose_name="Контактное лицо отдел рекламы")

    class Meta:
        verbose_name = 'Номера телефонов, эл. почты, контактные лица'
        verbose_name_plural = 'Номера телефонов, эл. почты, контактные лица'


class SocialNetwork(models.Model):
    """Социальные сети"""
    social_TG = models.CharField('Ссылка на Телеграм', max_length=250, blank=True, null=True)
    social_Youtube = models.CharField('Ссылка на YouTube', max_length=250, blank=True, null=True)
    social_Facebook = models.CharField('Ссылка на Фейсбук', max_length=250, blank=True, null=True)
    social_Instagram = models.CharField('Ссылка на Инстаграм', max_length=250, blank=True, null=True)
    social_VK = models.CharField('Ссылка на ВКонтакте', max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Ссылки на соцсети'
        verbose_name_plural = 'Ссылки на соцсети'

    def __str__(self):
        return 'Ссылки на соцсети'


class PaymentInfo(models.Model):
    """Реквизиты"""
    account1 = models.CharField('Р/с бюджет', max_length=50, blank=True, null=True)
    account2 = models.CharField('Р/с внебюджет', max_length=50, blank=True, null=True)
    UNP = models.CharField('УНП', max_length=10, blank=True, null=True)
    OKPO = models.CharField('ОКПО', max_length=10, blank=True, null=True)
    bank_name = models.CharField('Наименование банка', max_length=50, blank=True, null=True)
    bank_address = models.CharField('Адрес банка', max_length=70, blank=True, null=True)
    bank_BIC = models.CharField('БИК банка', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'


class Partner(models.Model):
    """Партнеры организации"""
    title = models.CharField('Партнер', max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='partners_logo/', verbose_name="Изображение", blank=True, null=True,)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.title


# class CategoryService(models.Model):
#     """Классификация услуг"""
#     # CHOICES_CATEGORY = (
#     #     ('футбольное поле', 'Футбольное поле'),
#     #     ('реклама', 'Реклама'),
#     #     ('спорт', 'Спорт'),
#     #     ('здоровье', 'Здоровье'),
#     #     ('организация мероприятий', 'Организация мероприятий'),
#     #     ('прочие услуги', 'Прочие услуги'),
#     # )
#     title = models.CharField('Категория услуги', max_length=40)
#     slug = models.SlugField(unique=True)
#
#     class Meta:
#         verbose_name = 'Категория услуги'
#         verbose_name_plural = 'Категории услуг'
#
#     def __str__(self):
#         return self.title


# class Service(models.Model):
#     """Услуги организации"""
#     category = models.ForeignKey(
#         'CategoryService',
#         on_delete=models.PROTECT,
#         verbose_name="Категория услуги"
#     )
#     title = models.CharField(max_length=200, verbose_name="Название услуги")
#     slug = models.SlugField(unique=True)
#     description = models.TextField(verbose_name="Полное описание")
#     brief_description = models.CharField(max_length=400, verbose_name="Краткое описание")
#     price_with_VTA = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Тариф с НДС", default=0)
#     price_without_VTA = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Тариф без НДС", default=0)
#     image = models.ImageField(upload_to='services/', verbose_name="Изображение", blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Услуга'
#         verbose_name_plural = 'Услуги'
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('main:service_detail', args=[self.id])
#
#
class UserEmail(models.Model):
    """Электронный адрес пользователя, который хочет получать уведомления о новостях"""
    email = models.EmailField(blank=False, verbose_name='Электронная почта клиента')

    class Meta:
        verbose_name = 'Адрес электронной почты клиента'
        verbose_name_plural = 'Адреса электронной почты клиентов'

    def __str__(self):
        return self.email
#
#
# class Order(models.Model):
#     """Заявка перезвонить от клиента"""
#     CHOICES_STATUS = (
#         ('в обработке', 'в обработке'),
#         ('новая заявка', 'новая заявка'),
#         ('обработана', 'обработана'),
#     )
#     name = models.CharField(max_length=60,  verbose_name="Имя клиента")
#     phone_number = models.CharField('Номер телефона', max_length=30)
#     status = models.CharField('Статус заявки', max_length=20, choices=CHOICES_STATUS, default='новая заявка')
#     data = models.DateTimeField('Дата и время заявки', auto_now_add=True)
#
#     class Meta:
#         ordering = ['-data']
#         verbose_name = 'Заявка'
#         verbose_name_plural = 'Заявки'
#
#     def __str__(self):
#         return f'{self.name},{self.phone_number}'