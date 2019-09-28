from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View 
from user_profile.models import User
from .models import Tweet

class Index(View):

	def get(self, request):

		form = NameForm()

		params={}

		params["name"]="Django"

		return render(request,"base.html",params)

	def post(self, request):

		return HttpResponse('I am called from a post request')









