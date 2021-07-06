from . import views
from django.urls import path
from .views import current_user, UserList
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Anime_Creator_App'
urlpatterns = [
    path('comments/', views.CommentView.as_view(), name='comments'),
    path('ratings/', views.RatingView.as_view(), name='ratings'),
    path('ratings/<int:id>/', views.RatingView.as_view(), name='rating'),
    path('videos/', views.VideoView.as_view(), name='videos'),
    path('creators/', views.AnimeCreatorView.as_view(), name='creators'),
    path('creators/<int:id>/', views.AnimeCreatorView.as_view(), name="creator"),
    path('comments/<int:id>/', views.CommentView.as_view(), name='comment'),
    path('videos/<str:name>/', views.VideoViewDetail.as_view(), name='videos'),
    path('friends/', views.FriendsView.as_view(), name='friends'),
    path('friends/<int:id>/', views.FriendsView.as_view(), name='friend'),
    path('friendssearch/', views.AnimeCreatorFriendsView.as_view(), name='friendssearch'),
    path('message/', views.MessageView.as_view(), name='message'),
    path('message/<int:id>/', views.MessageView.as_view(), name='message'),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
