from . import views
from django.urls import path


app_name = 'Anime_Creator_App'
urlpatterns = [
    path('', views.index, name='index'),
]