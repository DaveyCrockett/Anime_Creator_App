from django.shortcuts import render
from django.http import HttpResponse
from .models import AnimeCreator, Comment, Rating
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def index(request):
    all_creators = AnimeCreator.objects.all()
    context = {
        'all_creators': all_creators
    }
    return render(request, 'Anime_Creator_App/index.html', context)


class CommentList(APIView):

    def get(self, request):
        if request.method == 'GET':
            comments = Comment.objects.all()
            currentComments = request.query_params.get('currentComments', None)
            if currentComments is not None:
                comments = comments.filter(currentComments_icontains=currentComments)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
