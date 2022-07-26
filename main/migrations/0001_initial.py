# Generated by Django 4.0.6 on 2022-07-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_phone_main', models.CharField(max_length=30, verbose_name='Общий номер телефона')),
                ('email_main', models.EmailField(max_length=254, verbose_name='Общая электронная почта организации')),
                ('number_phone_reception', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер приемной')),
                ('email_reception_1', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта приемной №1')),
                ('email_reception_2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта приемной №2')),
                ('contact_person_reception', models.CharField(blank=True, max_length=200, null=True, verbose_name='Контактное лицо приемная')),
                ('number_phone_ad', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер отдела рекламы')),
                ('email_ad', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта отдела рекламы')),
                ('contact_person_ad', models.CharField(blank=True, max_length=200, null=True, verbose_name='Контактное лицо отдел рекламы')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Партнер')),
                ('image', models.ImageField(blank=True, null=True, upload_to='partners_logo/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Партнер',
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Р/с бюджет')),
                ('account2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Р/с внебюджет')),
                ('UNP', models.CharField(blank=True, max_length=10, null=True, verbose_name='УНП')),
                ('OKPO', models.CharField(blank=True, max_length=10, null=True, verbose_name='ОКПО')),
                ('bank_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Наименование банка')),
                ('bank_address', models.CharField(blank=True, max_length=70, null=True, verbose_name='Адрес банка')),
                ('bank_BIC', models.CharField(blank=True, max_length=50, null=True, verbose_name='БИК банка')),
            ],
            options={
                'verbose_name': 'Реквизиты',
                'verbose_name_plural': 'Реквизиты',
            },
        ),
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_TG', models.CharField(blank=True, max_length=250, null=True, verbose_name='Социальная сеть Телеграмм')),
                ('social_Youtube', models.CharField(blank=True, max_length=250, null=True, verbose_name='Социальная сеть YouTube')),
                ('social_Facebook', models.CharField(blank=True, max_length=250, null=True, verbose_name='Социальная сеть Фейсбук')),
                ('social_Instagram', models.CharField(blank=True, max_length=250, null=True, verbose_name='Социальная сеть Инстаграм')),
                ('social_VK', models.CharField(blank=True, max_length=250, null=True, verbose_name='Социальная сеть ВКонтакте')),
            ],
            options={
                'verbose_name': 'Соцсеть',
                'verbose_name_plural': 'Соцсети',
            },
        ),
    ]
