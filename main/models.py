from django.db import models


class Contact(models.Model):
    """Контакты организации"""
    number_phone_main = models.CharField('Общий номер телефона', max_length=30, blank=False)
    email_main = models.EmailField(blank=False, verbose_name='Общая электронная почта организации')

    number_phone_reception = models.CharField('Номер тел. приемной', max_length=30, blank=True, null=True)
    email_reception_1 = models.EmailField(blank=True, null=True, verbose_name='Электронная почта №1 приемная')
    email_reception_2 = models.EmailField(blank=True, null=True, verbose_name='Электронная почта №2 приемная')
    contact_person_reception = models.CharField(max_length=200, blank=True, null=True,
                                                verbose_name="Контактное лицо приемная")

    number_phone_ad = models.CharField('Номер тел. отдел рекламы', max_length=30, blank=True, null=True)
    email_ad = models.EmailField(blank=True, null=True, verbose_name='Электронная почта отдел рекламы')
    contact_person_ad = models.CharField(max_length=200, blank=True, null=True,
                                         verbose_name="Контактное лицо отдел рекламы")

    number_phone_personnel = models.CharField('Номер тел. отдел кадров', max_length=30, blank=True, null=True)
    email_personnel = models.EmailField(blank=True, null=True, verbose_name='Электронная почта отдел кадров')
    contact_person_personnel = models.CharField(max_length=200, blank=True, null=True,
                                         verbose_name="Контактное лицо отдел кадров")

    class Meta:
        verbose_name = 'Номера телефонов, эл.почты, контактных лиц'
        verbose_name_plural = 'Номера телефонов, эл. почты, контактные лица'

    def __str__(self):
        return 'Контактная информация'


class SocialNetwork(models.Model):
    """Социальные сети"""
    social_TG = models.CharField('Ссылка на Телеграм', max_length=250, blank=True, null=True)
    social_Youtube = models.CharField('Ссылка на YouTube', max_length=250, blank=True, null=True)
    social_Facebook = models.CharField('Ссылка на Фейсбук', max_length=250, blank=True, null=True)
    social_Instagram = models.CharField('Ссылка на Инстаграм', max_length=250, blank=True, null=True)
    social_VK = models.CharField('Ссылка на ВКонтакте', max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Ссылку на соцсеть'
        verbose_name_plural = 'Ссылки на соцсети'

    def __str__(self):
        return 'Ссылки на соцсети'


class Video(models.Model):
    """Видео на первой странице"""
    url = models.CharField(max_length=100, verbose_name='Видео для главной страницы')

    class Meta:
        verbose_name = 'Ссылку на видео'
        verbose_name_plural = 'Ссылки на видео'

    def __str__(self):
        return 'Ссылки на видео для главной страницы'


class VideoAdditional(models.Model):
    """Дополнительные видео для первой страницы"""
    urls = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        verbose_name='Видео'
    )
    video = models.CharField('Ссылка на дополнительное видео', max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Ссылку на видео'
        verbose_name_plural = 'Ссылки на видео'

    def __str__(self):
        return 'Ссылки на видео для главной страницы'


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
        verbose_name = 'Реквизиты для оплаты'
        verbose_name_plural = 'Реквизиты для оплаты'


class Partner(models.Model):
    """Партнеры организации"""
    title = models.CharField('Партнер', max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='partners_logo/', verbose_name="Изображение", blank=True, null=True, )

    class Meta:
        verbose_name = 'Партнера'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.title


class UserEmail(models.Model):
    """Электронный адрес пользователя, который хочет получать уведомления о новостях"""
    email = models.EmailField(blank=False, verbose_name='Электронная почта клиента')

    # created = models.DateTimeField(auto_now_add=True, verbose_name="Дата получения эл.почты от клиента")

    class Meta:
        verbose_name = 'Электронную почту клиента'
        verbose_name_plural = 'Электронные почты клиентов'

    def __str__(self):
        return self.email
