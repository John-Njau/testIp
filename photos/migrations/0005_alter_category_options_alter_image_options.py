# Generated by Django 4.0.4 on 2022-05-27 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_image_category_image_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'category'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-dated',)},
        ),
    ]