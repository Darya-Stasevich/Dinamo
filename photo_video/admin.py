from django.contrib import admin

from photo_video.models import PhotoLibrary, PhotoCategory, VideoLibrary, VideoCategory

#
# class PhotoCategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#

class PhotoImageInline(admin.StackedInline):
    model = PhotoLibrary
    verbose_name_plural = "Фотографии"
    verbose_name = "экземпляр Фотографии"


class VideoURLInline(admin.StackedInline):
    model = VideoLibrary
    verbose_name_plural = 'Видео'
    verbose_name = 'URL Видео'


class VideoLibraryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', )
    inlines = (VideoURLInline, )


class PhotoLibraryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', )
    inlines = (PhotoImageInline, )


admin.site.register(PhotoCategory, PhotoLibraryAdmin)
admin.site.register(VideoCategory, VideoLibraryAdmin)



