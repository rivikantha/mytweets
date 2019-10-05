from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.template import Context
from django.views.generic import View 
from user_profile.models import User
from .models import Tweet
from .forms import TweetForm
from .forms import SearchForm
from .models import Hashtag
import json

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

class Search(View):

	"""Search all tweets with query /search/?query=<query> URL"""

	def get(self, request):

		form = SearchForm()

		params = {}

		params['search'] = form

		if 'AJAX' in request.GET:

			query = request.GET.get('query','')

			tweets = Tweet.objects.filter(text__icontains=query)

			context = {"query": query, "tweets": tweets}
			
			return render_to_response('partials/_tweet_search.html',context)			

		return render(request,"tweets/search.html",params)


	def post(self, request):

		form = SearchForm(request.POST)

		if form.is_valid():

			query = form.cleaned_data['query']
			tweets = Tweet.objects.filter(text__icontains=query)
			context = {"query": query, "tweets": tweets}

			return_str = render_to_string('partials/_tweet_search.html',context)

			return HttpResponse(json.dumps(return_str),content_type="application/json")

		else:

			return HttpResponseRedirect("/search")
















					
			
		

			












