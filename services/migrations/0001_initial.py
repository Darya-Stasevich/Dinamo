# Generated by Django 4.0.6 on 2022-09-09 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/', verbose_name='Файл')),
                ('title', models.CharField(max_length=50, verbose_name='Название файла')),
                ('description', models.CharField(max_length=100, verbose_name='Краткое описание')),
            ],
            options={
                'verbose_name': 'Файл для услуги',
                'verbose_name_plural': 'Файлы для услуги',
            },
        ),
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Футбольное поле', 'Футбольное поле'), ('Реклама', 'Реклама'), ('Спорт', 'Спорт'), ('Здоровье', 'Здоровье'), ('Организация мероприятий', 'Организация мероприятий'), ('Прочие услуги', 'Прочие услуги')], max_length=40, verbose_name='Категория услуги')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категорию услуг',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя клиента')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('в обработке', 'в обработке'), ('новая заявка', 'новая заявка'), ('обработана', 'обработана')], default='новая заявка', max_length=20, verbose_name='Статус заявки')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заявки')),
            ],
            options={
                'verbose_name': 'Заявку',
                'verbose_name_plural': 'ЗАЯВКИ ПЕРЕЗВОНИТЬ',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('slug', models.SlugField(unique=True)),
                ('brief_description', models.CharField(max_length=400, verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Полное описание')),
                ('price_with_VAT_for_person', models.CharField(blank=True, default=0, help_text='Можно дописывать, например, "от", "индивидуально" и т.п.', max_length=50, null=True, verbose_name='Тариф с НДС для физ.лица')),
                ('price_without_VAT_for_person', models.CharField(blank=True, default=0, help_text='Можно дописывать, например, "от", "индивидуально" и т.п.', max_length=50, null=True, verbose_name='Тариф без НДС для физ.лица')),
                ('price_with_VAT_for_legal', models.CharField(blank=True, default=0, help_text='Можно дописывать, например, "от", "индивидуально" и т.п.', max_length=50, null=True, verbose_name='Тариф с НДС для юр.лица')),
                ('price_without_VAT_for_legal', models.CharField(blank=True, default=0, help_text='Можно дописывать, например, "от", "индивидуально" и т.п.', max_length=50, null=True, verbose_name='Тариф без НДС для юр.лица')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ед.измерения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Изображение')),
                ('published', models.BooleanField(default=True, verbose_name='Добавить на сайт')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления услуги')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования услуги')),
                ('is_primary_service', models.BooleanField(default=False, help_text='При наличии галочки данная услуга попадет в большой блок ЛУЧШИЕ УСЛУГИ ДЛЯ ВАС', verbose_name='Приоритетная услуга для отображения')),
                ('attachment', models.ForeignKey(blank=True, help_text='Если нужно прикрепить доп.информацию по услуге', null=True, on_delete=django.db.models.deletion.CASCADE, to='services.attachment', verbose_name='Прикрепленный файл')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.categoryservice', verbose_name='Категория услуги')),
            ],
            options={
                'verbose_name': 'Услугу',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
