# Generated by Django 3.1.8 on 2021-06-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anime_Creator_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default=None, upload_to='videos/'),
            preserve_default=False,
        ),
    ]
