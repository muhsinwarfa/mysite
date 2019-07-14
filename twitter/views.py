from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate, login
from .models import Tweet,Activity,Follower

# Create your views here.

# def index(request):
#     return render(request, 'twitterviews/index.html')

def list_tweets(request):
    tweets= Tweet.objects.all()
    return render(request, 'twitterviews/index.html', {'tweets': tweets})

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username= username, password= password)
            login(request,user)
            return redirect('http://127.0.0.1:8000/twitter/')

    else:
         form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html' , context)



