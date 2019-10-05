"""mytweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from tweets.views import Index, PostTweet, HashtagCloud, Search
from user_profile.views import Profile
from django.urls import path, re_path

admin.autodiscover()

urlpatterns = [
    path('', Index.as_view()),
    path('admin/', admin.site.urls),
    re_path(r'^user/(\w+)/$', Profile.as_view()),
    re_path(r'^user/(\w+)/post/$',PostTweet.as_view()),
    re_path(r'^hashtag/(\w+)/$',HashtagCloud.as_view()),
    re_path(r'^search/$', Search.as_view()),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]
