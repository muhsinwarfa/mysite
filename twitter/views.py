from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate, login
from .models import Tweet,Activity,Follower
from .forms import TweetForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

# def index(request):
#     return render(request, 'twitterviews/index.html')

@login_required
def list_tweets(request):
    tweets= Tweet.objects.all()
    return render(request, 'twitterviews/index.html', {'tweets': tweets})

@login_required
def create_tweet(request):
     if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
        return redirect('list_tweets')
     form = TweetForm()
     return render(request, 'twitterviews/newtweetform.html', {'form': form})


@login_required
def view_tweet(request,id):
    tweet = Tweet.objects.get(tweet_id=id)
    context= {'tweet': tweet}
    return render(request, 'twitterviews/view.html', context)

@login_required
def delete_tweet(request,id):
    tweet = Tweet.objects.get(tweet_id=id)
    tweet.delete()
    return redirect('list_tweets')

@login_required
def profile(request):
    if request.method == 'POST':
        print("hi")
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print(p_form)
        print(u_form)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            print("works fine")
            redirect('list_tweets')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'twitterviews/profile.html', context)

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


