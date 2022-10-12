from django.db import models, transaction
from django.db.models import UniqueConstraint, Q
from django.urls import reverse


class CategoryService(models.Model):
    """Классификация услуг"""
    FIELD = 'Футбольное поле'
    AD = 'Реклама'
    SPORT = 'Спорт'
    HEALTH = 'Здоровье'
    EVENT = 'Организация мероприятий'
    OTHERS = 'Прочие услуги'

    CHOICES_CATEGORY = (
        (FIELD, 'Футбольное поле'),
        (AD, 'Реклама'),
        (SPORT, 'Спорт'),
        (HEALTH, 'Здоровье'),
        (EVENT, 'Организация мероприятий'),
        (OTHERS, 'Прочие услуги'),
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
        verbose_name="Категория услуги", related_name='services'
    )
    title = models.CharField(max_length=100, verbose_name="Название услуги")
    slug = models.SlugField(unique=True)
    brief_description = models.CharField(max_length=400, verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Полное описание")

    price_with_VAT_for_person = models.CharField(max_length=50, verbose_name="Тариф с НДС для физ.лица", default=0,
                                                 help_text='Пример заполнения: "от 600 BYN", "индивидуально" и т.п.')
    price_without_VAT_for_person = models.CharField(max_length=50, default=0,
                                                    verbose_name="Тариф без НДС для физ.лица",
                                                    help_text='Пример заполнения: "от 600 BYN", "индивидуально" и т.п.')
    price_with_VAT_for_legal = models.CharField(max_length=50, default=0,
                                                verbose_name="Тариф с НДС для юр.лица",
                                                help_text='Пример заполнения: "от 600 BYN", "индивидуально" и т.п.')
    price_without_VAT_for_legal = models.CharField(max_length=50, default=0,
                                                   verbose_name="Тариф без НДС для юр.лица",
                                                   help_text='Пример заполнения: "от 600 BYN", "индивидуально" и т.п.')
    notes = models.CharField(max_length=200, verbose_name="Ед.измерения",
                             help_text='Пример заполнения: "шт.", "руб./час" и т.п.')
    image = models.ImageField(upload_to='services/', verbose_name="Изображение")
    published = models.BooleanField('Добавить на сайт', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления услуги")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата редактирования услуги")

    attachment = models.ForeignKey('Attachment', on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='Прикрепленный файл',
                                   help_text="Если нужно прикрепить доп.информацию по услуге")
    is_primary_service = models.BooleanField(default=False, verbose_name='Приоритетная услуга для отображения',
                                             help_text='При наличии галочки данная услуга попадет в большой блок ЛУЧШИЕ УСЛУГИ ДЛЯ ВАС')

    def save(self, *args, **kwargs):
        """Добавление только одной услуги с полем is_primary_service=True"""
        if not self.is_primary_service:
            return super(Service, self).save(*args, **kwargs)
        with transaction.atomic():
            Service.objects.filter(
                is_primary_service=True).update(is_primary_service=False)
            return super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Attachment(models.Model):
    """Прикрепленный файл с информацией об услуге"""
    file = models.FileField(upload_to="files/", verbose_name="Файл")
    title = models.CharField(max_length=100, verbose_name="Название файла",
                             help_text='Техническое задание на проведение мероприятия на территории Национального олимпийского стадиона «Динамо»"')
    description = models.CharField(max_length=50, verbose_name="Краткое описание",
                                   help_text='Пример заполения:"Скачать техническое задание"')

    class Meta:
        verbose_name = 'Файл для услуги'
        verbose_name_plural = 'Файлы для услуги'

    def __str__(self):
        return self.title


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
        verbose_name = 'Заявку'
        verbose_name_plural = 'ЗАЯВКИ ПЕРЕЗВОНИТЬ'

    def __str__(self):
        return f'{self.name},{self.phone_number}'
