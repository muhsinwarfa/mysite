from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  authenticate, login
from .models import Tweet,Activity,Follower,Profile
from .forms import TweetForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.

# def index(request):
#     return render(request, 'twitterviews/index.html')

@login_required
def list_tweets(request):
    # get all follower objects
    followers = Follower.objects.all()
    # store the user ids of the users that are being followed by the currently logged in user
    listofusers = []
    for follower in followers:
        if follower.user == request.user:
            listofusers.append(follower.user_id_2)
    # now list of users has all the ids the currently logged in user plus the id of the current user
    listofusers.append(request.user.id)
    tweets = Tweet.objects.filter(user__in=listofusers)
    context={
        'tweets': tweets
    }
    return render(request, 'twitterviews/index.html',context)


@login_required
def create_tweet(request):
     if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.is_tweet = 1
            obj.save()
        return redirect('list_tweets')
     form = TweetForm()

     return render(request, 'twitterviews/newtweetform.html', {'form': form})
#
# @login_required
# def create_retweet(request):
#
#
# @login_required
# def create_reply(request)


@login_required
def create_reply(request,id):
     # get the original tweet using the viewed tweet id
     original_tweet = Tweet.objects.get(tweet_id=id)
     if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            # fill in the respective fields for a reply tweet
            obj = form.save(commit=False)
            obj.user = request.user
            obj.is_reply = 1
            original_tweet.reply_count += 1
            original_tweet.save()
            obj.original_tweet_id = id
            obj.save()
        return redirect('list_tweets')
     form = TweetForm()
     context = {
         'form': form ,
         'id': id
     }

     return render(request, 'twitterviews/newreplyform.html', context)











@login_required
def view_tweet(request,id):
    tweet = Tweet.objects.get(tweet_id=id)
    replies = Tweet.objects.filter(original_tweet_id=id)
    context= {'tweet': tweet, 'replies': replies}
    return render(request, 'twitterviews/view.html', context)

@login_required
def delete_tweet(request,id):
    tweet = Tweet.objects.get(tweet_id=id)
    tweet.delete()
    return redirect('list_tweets')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            redirect('profile')
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


@login_required
def bio(request, username):
    user = User.objects.get(username=username)
    context = {
        'user': user,
    }
    return render(request,'twitterviews/bio.html',context)

def follow(request,username):
    user = User.objects.get(username=username)
    follow = Follower()
    follow.user = request.user
    follow.user_id_2 = user.id
    follow.save()
    redirect(request,"twitterviews/bio.html")

def unfollow(request,username):
    user_to_be_unfollowed = User.objects.get(username=username)
    unfollow_obj = Follower(request.user,user_to_be_unfollowed.id)
    unfollow_obj.delete()
    redirect(request,"twitterviews/bio.html")


