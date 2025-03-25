from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from casks.models import (
    Casks,
    Manufacturer,
    CaskVolumeCategory,
    TypeOfWood,
    CaskType,
)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'website',
        'slug',
    )
    list_filter = ('name', 'location')
    search_fields = ('name', 'location')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CaskVolumeCategory)
class CaskVolumeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'slug',
    )
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(TypeOfWood)
class TypeOfWoodAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CaskType)
class CaskTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Casks)
class CasksAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        # 'owners',
        'image',
        'manufacturer',
        'volume',
        'category_of_volume',
        'type_of_wood',
        'start_of_operation',
        'stop_of_operation',
        'time_create',
        'time_update',
    )
    list_filter = ('manufacturer', 'volume')
    search_fields = ('manufacturer', 'volume')
    prepopulated_fields = {'slug': ('name', 'volume')}

    @admin.display(description='Изображение')
    def image_preview(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" />')
