# Generated by Django 2.2 on 2020-05-16 07:17

import detection.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=detection.models.get_detection_image_path, verbose_name='推論用画像を選択')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
