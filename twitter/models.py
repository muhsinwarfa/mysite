from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweet_id  = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    tweet_text = models.CharField(max_length= 150)
    time_posted = models.DateField()
    is_retweet = models.BooleanField()
    is_tweet = models.BooleanField()
    is_reply = models.BooleanField()
    like_count = models.IntegerField()
    retweet_count = models.IntegerField()
    reply_count = models.IntegerField()
    original_tweet_id = models.IntegerField()




class Activity(models.Model):
    activity_id =
    user_id = models.IntegerField()
    activity_name = models.CharField(max_length=50)
    user_id_2 = models.IntegerField()
    date_time = models.DateField()

class Follower(models.Model):
    user_id = models.IntegerField()
    user_id_2 = models.IntegerField()
