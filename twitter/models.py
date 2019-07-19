from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import date


# Create your models here.
class Tweet(models.Model):
    tweet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    tweet_text = models.CharField(max_length= 150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_retweet = models.IntegerField(default='0', null=True, blank=True)
    is_tweet = models.IntegerField(default='0', null=True, blank=True)
    is_reply = models.IntegerField(default='0',null=True, blank=True)
    like_count = models.IntegerField(default='0',null=True, blank=True)
    retweet_count = models.IntegerField(default='0',null=True, blank=True)
    reply_count = models.IntegerField(default='0',null=True, blank=True)
    original_tweet_id = models.IntegerField(null=True, blank=True)

class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=50)
    user_id_2 = models.IntegerField()
    date_time = models.DateField()


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id_1 = models.IntegerField(default='1')
    user_id_2 = models.IntegerField(default='2')


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)





