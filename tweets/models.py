from django.db import models
from user_profile.models import User

class Tweet(models.Model):

	"""
	Tweet Model
	"""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=160)
	created_date = models.DateTimeField(auto_now_add=True)
	country = models.CharField(max_length=30)
	is_active = models.BooleanField(default=True)

	def __str__(self):

		return self.text

class Hashtag(models.Model):

	"""
	Hashtag Model
	"""

	name = models.CharField(max_length=64, unique=True)

	tweet = models.ManyToManyField(Tweet)

	def __str__(self):

		return self.name


class UserFollowers(models.Model):

	user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	count = models.IntegerField(default=1)
	followers = models.ManyToManyField(User,related_name="followers")
	
	def __str__(self):
		return '%s, %s' % self.user, self.count
	
