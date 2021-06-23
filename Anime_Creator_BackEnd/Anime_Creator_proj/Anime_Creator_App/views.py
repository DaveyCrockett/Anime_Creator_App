from django.shortcuts import render
from django.http import HttpResponse
from .models import AnimeCreator, Comment, Rating
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CommentSerializer, RatingSerializer, AnimeCreatorSerializer
from django.http import Http404

# Create your views here.


def index(request):
    all_creators = AnimeCreator.objects.all()
    context = {
        'all_creators': all_creators
    }
    return render(request, 'Anime_Creator_App/index.html', context)


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

    def delete(self, request, comment_id):
        comment = self.get_object(pk=comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

