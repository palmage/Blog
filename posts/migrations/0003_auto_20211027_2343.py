# Generated by Django 3.2.8 on 2021-10-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211027_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comments_images/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts_images/', verbose_name='Изображение'),
        ),
    ]
