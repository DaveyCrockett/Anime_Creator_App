from rest_framework import serializers
from .models import Comment, Rating, AnimeCreator


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']
        
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating']
        
        
class AnimeCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeCreator
        fields = ['username', 'password', 'email']
        