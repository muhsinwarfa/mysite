from django import forms
from twitter.models import Tweet
from django.contrib.auth.models import User
from .models import Profile,Follower

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        exclude = ('user',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class FollowerForm(forms.ModelForm):
    user_id_2 = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    class Meta:
        model = Follower
        exclude = ('user',)
