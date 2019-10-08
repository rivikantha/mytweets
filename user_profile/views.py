from django.shortcuts import render
from django.views.generic import View 
from user_profile.models import User
from tweets.models import Tweet,UserFollowers
from tweets.forms import TweetForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Profile(LoginRequiredMixin,View):

	""" User profile page reached from /user/<username> """

	login_url = '/login/'
	redirect_field_name = 'redirect_to'

	def get(self,request,username):

		params = {}

		profile = User.objects.get(username=username)
		user=request.user

		try:
			userFollower = UserFollowers.objects.get(user=profile)

			if userFollower.followers.filter(username=user.username).exists():

				params['following'] = True

			else:

				params['following'] = False

		except:

			params['following'] = False		

		tweets = Tweet.objects.filter(user=profile)
		
		params["tweets"] = tweets
		params['user'] = user
		params["profile"] = profile
		params["name"] = "MyTweets / "+user.username
		params["form"] = TweetForm(initial={'country': 'Global'})
		return render(request, 'user_profile/profile.html', params)
