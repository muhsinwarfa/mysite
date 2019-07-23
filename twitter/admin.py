from django.contrib import admin
from .models import Tweet
from .models import Profile
from .models import Follower
from .models import Activity

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Profile)
admin.site.register(Follower)
admin.site.register(Activity)