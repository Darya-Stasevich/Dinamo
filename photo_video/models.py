# from django.db import models
#
#
# class PhotoCategory(models.Model):
#     """Раздел фотоальбома"""
#     title = models.CharField(max_length=200, verbose_name="Раздел фотоальбома")
#     cover = models.ImageField(upload_to='photo_library/covers', verbose_name="Изображение обложки", blank=True)
#
#     class Meta:
#         verbose_name = 'Раздел фотоальбома'
#         verbose_name_plural = 'Разделы фотоальбома'
#
#     def __str__(self):
#         return self.title
#
#
# class PhotoLibrary(models.Model):
#     """Фотоальбом"""
#     category = models.ForeignKey('PhotoCategory', on_delete=models.CASCADE, verbose_name="Раздел фотоальбома")
#     image = models.ImageField(upload_to='photo_library/covers', verbose_name="Изображение обложки", blank=True)
#     #  добавлять несколько фоток
#
#     class Meta:
#         verbose_name = 'Фотоальбом'
#         verbose_name_plural = 'Фотоальбомы'
#
#
# class VideoCategory(models.Model):
#     """Раздел видеоальбома"""
#     title = models.CharField(max_length=200, verbose_name="Рубрика видео")
#     cover = models.ImageField(upload_to='video_library/covers', verbose_name="Обложки для видео", blank=True)
#
#     class Meta:
#         verbose_name = 'Раздел видеоальбома'
#         verbose_name_plural = 'Разделы видеоальбома'
#
#     def __str__(self):
#         return self.title
#
# class VideoLibrary(models.Model):
#     category = models.ForeignKey('VideoCategory', on_delete=models.CASCADE, verbose_name="Раздел видеоальбома")
#     path = models.CharField(max_length=200, verbose_name="Ссылка на видео")