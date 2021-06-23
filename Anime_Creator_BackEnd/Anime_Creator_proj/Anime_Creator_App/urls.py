from . import views
from django.urls import path


app_name = 'Anime_Creator_App'
urlpatterns = [
    path('', views.index, name='index'),
    path('comments/', views.CommentView.as_view(), name='comments'),
    path('ratings/', views.RatingView.as_view(), name='ratings')
]