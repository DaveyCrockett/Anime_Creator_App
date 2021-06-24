# Generated by Django 3.1.8 on 2021-06-24 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Anime_Creator_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anime_Creator_App.animecreator')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anime_Creator_App.video')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Anime_Creator_App.video')),
            ],
        ),
    ]
