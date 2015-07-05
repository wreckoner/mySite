from django.conf.urls import include, url
from .views import trends, twitter_trends_closest


urlpatterns = [
	url(r'^$', trends),
	url(r'^twitter_trends_closest', twitter_trends_closest),
]