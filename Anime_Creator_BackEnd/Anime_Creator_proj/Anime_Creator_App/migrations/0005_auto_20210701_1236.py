# Generated by Django 3.1.8 on 2021-07-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anime_Creator_App', '0004_auto_20210701_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='http://127.0.0.1:8000/Anime_Creator_App/upload/'),
        ),
    ]
