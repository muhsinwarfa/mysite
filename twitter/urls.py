from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index , name = 'twitter'),
    path('', views.list_tweets, name=''),
    # path('new', views.create_tweet, name='create_tweet'),
    # path('update/<int:id>', views.update_tweet, name='update_tweet'),
    # path('delete/<int:id>', views.delete_tweet, name='delete_tweet'),
    # path('accounts/', views.index, name= 'login'),
    path('register', views.registration, name= 'register'),
]