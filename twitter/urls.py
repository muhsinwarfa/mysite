from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.list_tweets, name= 'list_tweets'),
    path('new', views.create_tweet, name='create_tweet'),
    path('delete/<int:id>', views.delete_tweet, name='delete_tweet'),
    path('view/<int:id>', views.view_tweet, name='view_tweet'),
    path('register', views.registration, name='register'),
    path('profile',views.profile,name='profile'),
    path('bio/<username>',views.bio, name='bio_page'),
    path('view/<int:id>/reply',views.create_reply,name='create_reply'),
    path('view/<int:id>/retweet', views.create_retweet, name='create_retweet')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
