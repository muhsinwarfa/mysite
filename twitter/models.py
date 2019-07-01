from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Tweet(models.Model):
    tweet_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length= 150)
    time_posted = models.DateField()
    is_retweet = models.IntegerField()
    is_tweet = models.IntegerField()
    is_reply = models.IntegerField()
    like_count = models.IntegerField()
    retweet_count = models.IntegerField()
    reply_count = models.IntegerField()
    original_tweet_id = models.IntegerField()

class Activity(models.Model):
    activity_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    activity_name = models.CharField(max_length=50)
    user_id_2 = models.IntegerField()
    date_time = models.DateField()


class Follower(models.Model):
    user_id = models.IntegerField()
    user_id_2 = models.IntegerField()
