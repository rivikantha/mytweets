from django.shortcuts import render
from django.views.generic import View 
from user_profile.models import User
from tweets.models import Tweet,UserFollowers
from tweets.forms import TweetForm
from django.http import HttpResponse
import json
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
		
		ipdb.set_trace()
		
		params["tweets"] = tweets
		params['user'] = user
		params["profile"] = profile
		params["name"] = "MyTweets / "+user.username
		params["form"] = TweetForm(initial={'country': 'Global'})
		return render(request, 'user_profile/profile.html', params)

	def post(self,request,username):

		"""Post ot add followers reached from /user/<username> """

		follow = request.POST['follow']

		user = request.user

		userProfile = User.objects.get(username=username)

		userFollower,status = UserFollowers.objects.get_or_create(user=userProfile)

		if follow =='true':

			userFollower.followers.add(user)

		else:

			userFollower.followers.remove(user)

		return HttpResponse(json.dumps(""),content_type="application/json")

class MostFollowedUsers(View):

	def get(self,request):

		userFollowers = UserFollowers.objects.order_by('-count')

		params={}

		params['userFollowers']=userFollowers

		return render(request,'user_profile/users.html',params)










