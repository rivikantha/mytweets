from django.shortcuts import render
from django.views.generic import View 
from user_profile.models import User
from tweets.models import Tweet
from tweets.forms import TweetForm

class Profile(View):

	""" User profile page reached from /user/<username> """

	def get(self,request,username):

		params = {}

		user = User.objects.get(username=username)
		tweets = Tweet.objects.filter(user=user)

		params["tweets"] = tweets
		params["user"] = user
		params["name"] = "MyTweets / "+user.username
		params["form"] = TweetForm()
		return render(request, 'user_profile/profile.html', params)
