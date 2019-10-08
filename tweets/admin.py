from django.contrib import admin
from .models import Tweet,Hashtag,UserFollowers

admin.site.register(Tweet)
admin.site.register(Hashtag)
admin.site.register(UserFollowers)


