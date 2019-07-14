from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate, login
from .models import Tweet,Activity,Follower
from .forms import TweetForm

# Create your views here.

# def index(request):
#     return render(request, 'twitterviews/index.html')


def list_tweets(request):
    tweets= Tweet.objects.all()
    return render(request, 'twitterviews/index.html', {'tweets': tweets})


def create_tweet(request):

    form = TweetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_tweets')
    return render(request, 'twitterviews/newtweetform.html', {'form':form})


def delete_tweet(request,id):

    tweet= Tweet.objects.get(tweet_id=id)
    tweet.delete()
    return redirect('list_tweets')


# def view_tweet(request,id):
#     tweet = Tweet.objects.get(tweet_id=id)
#     return
def registration(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('list_tweets')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context )


