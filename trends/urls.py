from django.conf.urls import include, url
from .views import trends, twitter_trends_api


urlpatterns = [
	url(r'^$', trends),
	url(r'^twitter_trends_api', twitter_trends_api),
]