# Generated by Django 4.0.4 on 2022-05-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(upload_to='photos/static/uploads/'),
        ),
    ]
