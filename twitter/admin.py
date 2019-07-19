from django.contrib import admin
from .models import Tweet
from .models import Profile

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Profile)