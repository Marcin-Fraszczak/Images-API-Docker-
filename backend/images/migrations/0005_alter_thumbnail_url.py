# Generated by Django 4.1.5 on 2023-01-24 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnail',
            name='url',
            field=models.FileField(upload_to='resized_images/'),
        ),
    ]