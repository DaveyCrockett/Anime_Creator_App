from rest_framework import serializers
from .models import Comment, Rating, AnimeCreator, Video


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment']
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'rating']
        
        
class AnimeCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeCreator
        fields = ['id', 'username', 'password', 'email']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'name', 'description']
        