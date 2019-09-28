from django.contrib import admin
from .models import Tweet
from .models import Hashtag

admin.site.register(Tweet)
admin.site.register(Hashtag)

