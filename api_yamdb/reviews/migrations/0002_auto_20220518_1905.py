# Generated by Django 2.2.16 on 2022-05-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(help_text='Добавьте описание произведения', null=True, verbose_name='Описание'),
        ),
    ]