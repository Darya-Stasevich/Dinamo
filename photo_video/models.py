from django.db import models


class PhotoCategory(models.Model):
    """Раздел фотоальбома"""
    title = models.CharField(max_length=200, verbose_name="Раздел фотоальбома")
    slug = models.SlugField(unique=True)
    cover = models.ImageField(upload_to='photo_library/covers', verbose_name="Изображение обложки")

    class Meta:
        verbose_name = 'Раздел фотоальбома'
        verbose_name_plural = 'Разделы фотоальбомов'

    def __str__(self):
        return self.title


class PhotoLibrary(models.Model):
    """Фотографии"""
    title = models.CharField(max_length=100, verbose_name='Подпись фотографии', null=True, blank=True)
    category = models.ForeignKey('PhotoCategory', on_delete=models.CASCADE, related_name='photos',
                                 verbose_name="Раздел фотоальбома")
    image = models.ImageField(upload_to='photo_library/covers', verbose_name="Выберите фотографию", blank=True)

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'


class VideoCategory(models.Model):
    """Раздел видеоальбома"""
    title = models.CharField(max_length=200, verbose_name="Рубрика видео")
    slug = models.SlugField(unique=True)
    cover = models.ImageField(upload_to='video_library/covers', verbose_name="Обложки для видео")

    class Meta:
        verbose_name = 'Раздел видеоальбома'
        verbose_name_plural = 'Разделы видеоальбомов'

    def __str__(self):
        return self.title


class VideoLibrary(models.Model):
    """Видео"""
    title = models.CharField(max_length=100, verbose_name='Подпись видео', null=True, blank=True)
    category = models.ForeignKey('VideoCategory', on_delete=models.CASCADE, related_name='videos',
                                 verbose_name="Раздел видеоальбома")
    path = models.CharField(max_length=500, verbose_name="Ссылка на видео")

    def __str__(self):
        if self.title == None:
            return f'Без подписи'
        else:
            return f'{self.title}'
