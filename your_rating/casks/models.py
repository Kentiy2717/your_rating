from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from .constants import MAX_LENGTH_NAME, MAX_LENGTH_SLUG

User = get_user_model()

class Manufacturer(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Производитель'
    )
    location = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Местоположение'
    )
    website = models.URLField(
        verbose_name='Сайт'
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_SLUG,
        unique=True,
        db_index=True,
        verbose_name='manufacturer_URL'
    )

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('manufacturer_page', kwargs={'manufacturer_slug': self.slug})


class CaskVolumeCategory(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Тип древесины'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_SLUG,
        unique=True,
        db_index=True,
        verbose_name='volume_URL'
    )

    class Meta:
        verbose_name = 'Объем бочки'
        verbose_name_plural = 'Объемы бочек'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('volume_page', kwargs={'volume_slug': self.slug})


class TypeOfWood(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Тип древесины'
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_SLUG,
        unique=True,
        db_index=True,
        verbose_name='wood_URL'
    )

    class Meta:
        verbose_name = 'Тип древесины'
        verbose_name_plural = 'Типы древесины'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('wood_page', kwargs={'wood_slug': self.slug})


class CaskType(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Тип бочки'
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_SLUG,
        unique=True,
        db_index=True,
        verbose_name='cask_type_URL'
    )

    class Meta:
        verbose_name = 'Тип бочки'
        verbose_name_plural = 'Типы бочек'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cask_type_page', kwargs={'cask_type_slug': self.slug})


class Casks(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        verbose_name='Название',
        null=True,  # Вот тут пока вопрос надо ли оно.
        blank=True,  # Вот тут пока вопрос надо ли оно.
        help_text='Не обязательно.'
    )
    slug = models.SlugField(
        max_length=MAX_LENGTH_SLUG,
        unique=True,
        db_index=True,
        verbose_name='cask_URL'
    )
    owners = models.ManyToManyField(
        User,
        verbose_name='Владелецы',
        related_name='casks'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='casks/images/%Y/%m/%d/'
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        verbose_name='Производитель',
        related_name='casks'
    )
    volume = models.FloatField(
        verbose_name='Объем бочки',
        help_text='В литрах'
    )
    category_of_volume = models.ForeignKey(
        CaskVolumeCategory,
        on_delete=models.PROTECT,
        verbose_name='Объем бочки',
        blank=True,
        related_name='casks'
    )
    start_of_operation = models.DateField(
        verbose_name='Дата начала эксплуатации бочки',
    )
    stop_of_operation = models.DateField(
        verbose_name='Дата окончания эксплуатации бочки',
        null=True,
        blank=True,
        help_text='Оставьте пустым, если бочка еще в работе.'
    )
    type_of_wood = models.ForeignKey(
        TypeOfWood,
        on_delete=models.PROTECT,
        verbose_name='Тип древесины',
        related_name='casks'
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name='Время обновления'
    )

    class Meta:
        verbose_name = 'Бочка'
        verbose_name_plural = 'Бочки'
        ordering = ['-time_create']

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'Бочка {self.volume}л({self.manufacturer})'

    def get_absolute_url(self):
        return reverse('cask_page', kwargs={'cask_slug': self.slug})
