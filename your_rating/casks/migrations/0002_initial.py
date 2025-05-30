# Generated by Django 3.2.16 on 2025-03-25 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('casks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='casks',
            name='owners',
            field=models.ManyToManyField(related_name='casks', to=settings.AUTH_USER_MODEL, verbose_name='Владелецы'),
        ),
        migrations.AddField(
            model_name='casks',
            name='type_of_wood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='casks', to='casks.typeofwood', verbose_name='Тип древесины'),
        ),
    ]
