from django.conf.urls import include, url
from .views import trends, twitter_trends_api, update_woeids


urlpatterns = [
	url(r'^$', trends),
	url(r'^twitter_trends_api', twitter_trends_api),
	url(r'^update_woeids', update_woeids)
]