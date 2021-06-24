from . import views
from django.urls import path


app_name = 'Anime_Creator_App'
urlpatterns = [
    path('comments/', views.CommentView.as_view(), name='comments'),
    path('ratings/', views.RatingView.as_view(), name='ratings'),
    path('ratings/<int:id>', views.RatingView.as_view(), name='rating'),
    path('videos/', views.VideoView.as_view(), name='videos'),
    path('creators/', views.AnimeCreatorView.as_view(), name='creators'),
    path('creators/<int:id>', views.AnimeCreatorView.as_view(), name="creator"),
    path('comments/<int:id>', views.CommentView.as_view(), name='comment')
]