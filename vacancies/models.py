from django.db import models


class Vacancy(models.Model):
    title_of_vacancy = models.CharField(max_length=100, verbose_name='Название вакансии')
    salary = models.CharField(max_length=50, verbose_name='Зарплата', help_text='Пример заполнения: до 1500 бел.руб.')
    experience = models.CharField(max_length=50, verbose_name='Опыт работы',
                                  help_text='Пример заполнения: от 6 лет, до 1 года')
    employment = models.CharField(max_length=50, verbose_name='Занятость', help_text='Пример заполнения: полная занятость, 0,25 ставки')
    published = models.BooleanField(verbose_name='Опубликовать на сайте', default=True)

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'

    def __str__(self):
        return f'{self.title_of_vacancy}'


class VacancyRequirements(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название требования',
                             help_text='Например, ТРЕБОВАНИЯ, ОБЯЗАННОСТИ, ПРИВЕТСТВУЕТСЯ, ОПЫТ РАБОТЫ и т.д.')
    list_of_requirements = models.TextField(
        help_text=('Скопируйте этот тег в Пункты требования: &lt;li&gt;ВВЕДИТЕ ВАШ ТЕКСТ В ЭТОМ ТЕГЕ&lt;/li&gt;'),
        verbose_name='Пункты требования')
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, verbose_name='Вакансия',
                                related_name='requirements')


class FeedbackForVacancy(models.Model):
    STATUS = (
        ('in_process', 'В обработке'),
        ('new_request', 'Новая заявка'),
        ('reject', 'Отклонить'),
        ('recruit', 'Принять на работу'),
    )

    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    resume_file = models.FileField(verbose_name='Файл резюме', upload_to='./resumes/', blank=True, null=True)
    url_of_resume = models.CharField(max_length=250, verbose_name='ссылка на резюме', blank=True, null=True)
    status = models.CharField(max_length=15, choices=STATUS, default='new_request',
                              verbose_name='Статус заявки')
    date = models.DateTimeField(auto_now_add=True)
    vacancy = models.ForeignKey('Vacancy', verbose_name='Вакансия', on_delete=models.PROTECT)

    def __str__(self):
        return f''

    class Meta:
        verbose_name_plural = 'Отклики на вакансии'
        verbose_name = 'Отклик на вакансию'
