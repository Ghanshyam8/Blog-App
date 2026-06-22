from django.urls import path
from . import views


urlpatterns = [
    path('', views.tweet_list, name='tweetlist'),
    path('create/', views.tweet_create, name='tweetcreate'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweetedit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweetdelete'),
    path('register/', views.register, name='register'),
]
