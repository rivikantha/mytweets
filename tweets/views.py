from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View 
from user_profile.models import User
from .models import Tweet

class Index(View):

	def get(self, request):

		params={}

		params["name"]="Django"

		return render(request,"base.html",params)

	def post(self, request):

		return HttpResponse('I am called from a post request')


class Profile(View):

	""" User profile page reached from /user/<username> """

	def get(self,request,username):

		params = {}

		user = User.objects.get(username=username)
		tweets = Tweet.objects.filter(user=user)

		params["tweets"] = tweets
		params["user"] = user
		return render(request, 'profile.html', params)






