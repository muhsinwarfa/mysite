from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name = 'twitter'),
    # path('accounts/', views.index, name= 'login'),
    path('register', views.registration, name = 'register')
]