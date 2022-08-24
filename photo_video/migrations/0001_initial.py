#>>>>>>> 44ff7df21b7808d1f5bf27391f21be25214a80f7

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Раздел фотоальбома')),
                ('cover', models.ImageField(blank=True, upload_to='photo_library/covers', verbose_name='Изображение обложки')),
            ],
            options={
                'verbose_name': 'Раздел фотоальбома',
                'verbose_name_plural': 'Разделы фотоальбомов',
            },
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Рубрика видео')),
                ('cover', models.ImageField(blank=True, upload_to='video_library/covers', verbose_name='Обложки для видео')),
            ],
            options={
                'verbose_name': 'Раздел видеоальбома',
                'verbose_name_plural': 'Разделы видеоальбомов',
            },
        ),
        migrations.CreateModel(
            name='VideoLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Подпись видео')),
                ('path', models.CharField(max_length=500, verbose_name='Ссылка на видео')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo_video.videocategory', verbose_name='Раздел видеоальбома')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Подпись фотографии')),
                ('image', models.ImageField(blank=True, upload_to='photo_library/covers', verbose_name='Выберите фотографию')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo_video.photocategory', verbose_name='Раздел фотоальбома')),
            ],
        ),
    ]
