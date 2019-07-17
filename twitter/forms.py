from django import forms
from twitter.models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields =[ 'tweet_id' , 'user', 'tweet_text', 'is_retweet','is_tweet','is_reply','like_count'
                  ,'retweet_count','reply_count','original_tweet_id']
