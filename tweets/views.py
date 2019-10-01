from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import View 
from user_profile.models import User
from .models import Tweet
from .forms import TweetForm
from .models import Hashtag

class Index(View):

	def get(self, request):

		form = TweetForm()

		params={}

		params["name"]="Django"

		return render(request,"base.html",params)

	def post(self, request):

		return HttpResponse('I am called from a post request')


class PostTweet(View):

	"""Tweet Post form available on page /user/<username> URL"""

	def post(self, request, username):

		form = TweetForm(self.request.POST)

		params = {}	

		user = User.objects.get(username=username)	

		if form.is_valid():				

			tweet = Tweet(text=form.cleaned_data['text'],
				user=user,
				country=form.cleaned_data['country'])

			tweet.save()

			print(tweet)

			words = form.cleaned_data['text'].split(" ")

			for word in words:

				if word[0]=='#':

					hashtag, created = Hashtag.objects.get_or_create(name=word[1:])
					
					print(hashtag)
					print(created)

					hashtag.tweet.add(tweet)

		return HttpResponseRedirect('/user/'+username)

class HashtagCloud(View):

	"""Hash Tag page reachable from /hastag/<hashtag> URL"""

	def get(self, request, hashtag):

		params={}

		hashtag = Hashtag.objects.get(name=hashtag)

		params["tweets"] = hashtag.tweet

		return render(request, 'tweets/hashtag.html', params)





					
			
		

			












