# Generated by Django 3.2.16 on 2025-03-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casks', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Тип бочки')),
                ('slug', models.SlugField(unique=True, verbose_name='cask_type_URL')),
            ],
            options={
                'verbose_name': 'Тип бочки',
                'verbose_name_plural': 'Типы бочек',
            },
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='location',
            field=models.CharField(max_length=100, verbose_name='Местоположение'),
        ),
    ]
