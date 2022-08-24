from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_vacancy', models.CharField(max_length=100, unique=True, verbose_name='Название вакансии')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='VacancyRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название требования')),
                ('list_of_requirements', models.TextField(help_text='Скопируйте этот тег в Пункты требования: &lt;li&gt;ВВЕДИТЕ ВАШ ТЕКСТ В ЭТОМ ТЕГЕ&lt;/li&gt;', verbose_name='Пункты требования')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.vacancy', verbose_name='Вакансия')),
            ],
        ),
        migrations.CreateModel(
            name='MainInformationOfVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Информация о вакансии')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.vacancy', verbose_name='Вакансия')),
            ],
        ),
    ]
