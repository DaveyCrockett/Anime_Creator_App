from django.db import models

# Create your models here.


class AnimeCreator(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Comment(models.Model):
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.comment


class Rating(models.Model):
    rating = models.IntegerField()

