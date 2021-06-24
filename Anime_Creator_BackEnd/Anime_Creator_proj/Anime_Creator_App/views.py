from django.shortcuts import render
from django.http import HttpResponse
from .models import AnimeCreator, Comment, Rating, Video
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CommentSerializer, RatingSerializer, AnimeCreatorSerializer, VideoSerializer
from django.http import Http404

# Create your views here.


class CommentView(APIView):

    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        comment = self.get_object(pk=id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnimeCreatorView(APIView):

    def get_object(self, pk):
        try:
            return AnimeCreator.objects.get(pk=pk)
        except AnimeCreator.DoesNotExist:
            raise Http404

    def get(self, request, id):
        creator = self.get_object(pk=id)
        serializer = AnimeCreatorSerializer(creator)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        creator = self.get_object(pk=id)
        creator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = AnimeCreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingView(APIView):


    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            raise Http404

    def get(self, request, id):
        rating = self.get_object(pk=id)
        serializer = RatingSerializer(rating)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        rating = self.get_object(pk=id)
        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        rating = self.get_object(pk=id)
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_200_OK)


class VideoView(APIView):

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_all(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            raise Http404

    def delete(self, request, id):
        video = self.get_object(pk=id)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        video = self.get_object(pk=id)
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)