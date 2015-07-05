from datetime import timedelta
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone, dateparse
import tweepy

from .models import TwitterToken, TwitterTrend


# Create your views here.
def _trends(requests):
	TIME_SPAN_SECONDS = 30*60
	start_time = timezone.now()
	template = 'trends.html'
	context = {u'title' : u'Social media trends'}
	time_lapse = timezone.now() - TwitterTrend.objects.filter(location_id=1)[0].created_at
	if time_lapse.seconds > TIME_SPAN_SECONDS:
		try:
			tokens = TwitterToken.objects.all()[0]
			consumerKey = tokens.consumerKey
			consumerSecret = tokens.consumerSecret
			accessToken = tokens.accessToken
			accessTokenSecret = tokens.accessTokenSecret
			auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
			auth.set_access_token(accessToken, accessTokenSecret)
			api = tweepy.API(auth)
			data = api.trends_place(1)[0]
			context[u'twitter'] = data
			TwitterTrend().clean()
			TwitterTrend(location_id=data['locations'][0]['woeid'], trends=data, location=data['locations'][0]['name'], created_at=dateparse.parse_datetime(data['created_at'])).save()
			context[u'twitter_status'] = u'Retrieved trends from Twitter API and updated database.'
		except Exception, e:
			context[u'twitter'] = '. '.join([str(e), traceback.format_exc()])
			context[u'twitter_status'] = u'Failed to retrieve trends.'			
	else:
		context[u'twitter'] = TwitterTrend.objects.filter(location_id=1)[0].trends
		context[u'twitter_status'] = 'Trends retrieved within last 30 minutes. Showing cached result.'
	context['time_taken'] = timezone.now() - start_time
	return render(requests, template, context)

def trends(request):
	template = 'trends.html'
	context = {u'title' : u'Social Network Trends'}
	return render(request, template, context)



def twitter_trends_api(requests):
	TIME_SPAN_SECONDS = 30*60
	CACHE_FLAG = True
	context = {u'title' : u'Social media trends'}
	start_time = timezone.now()
	cached_data = TwitterTrend.objects.filter(location_id=int(requests.GET['WOEID']))
	if len(cached_data) == 0 or (timezone.now() - cached_data[0].created_at).seconds > TIME_SPAN_SECONDS:
		CACHE_FLAG = False
		try:
			tokens = TwitterToken.objects.all()[0]
			consumerKey = tokens.consumerKey
			consumerSecret = tokens.consumerSecret
			accessToken = tokens.accessToken
			accessTokenSecret = tokens.accessTokenSecret
			auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
			auth.set_access_token(accessToken, accessTokenSecret)
			api = tweepy.API(auth)
			data = api.trends_place(int(requests.GET['WOEID']))[0]
			context[u'twitter'] = data
			TwitterTrend().clean()
			TwitterTrend(location_id=data['locations'][0]['woeid'], trends=data, location=data['locations'][0]['name'], created_at=dateparse.parse_datetime(data['created_at'])).save()
			context[u'twitter_status'] = u'Retrieved trends from Twitter API and updated database.'
		except Exception, e:
			context[u'twitter'] = '. '.join([str(e), traceback.format_exc()])
			context[u'twitter_status'] = u'Failed to retrieve trends.'
	else:
		context[u'twitter'] = cached_data[0].trends
		context[u'twitter_status'] = 'Trends retrieved within last 30 minutes. Showing cached result.'
	return JsonResponse(context)