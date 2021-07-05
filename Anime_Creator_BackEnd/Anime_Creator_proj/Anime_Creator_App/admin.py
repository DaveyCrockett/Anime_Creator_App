from django.contrib import admin
from .models import AnimeCreator, Video, Comment, Rating, Friends, Message

# Register your models here.
admin.site.register(AnimeCreator)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Friends)
admin.site.register(Message)
