# Generated by Django 2.2 on 2020-05-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='result',
            field=models.CharField(default='/media/images', max_length=500),
        ),
    ]
