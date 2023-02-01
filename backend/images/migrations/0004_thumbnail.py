# Generated by Django 4.1.5 on 2023-01-24 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='rezsized_images/')),
                ('height', models.PositiveIntegerField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnails', to='images.image')),
            ],
        ),
    ]
