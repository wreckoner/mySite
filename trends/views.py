from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone, dateparse
from datetime import timedelta
from .models import TwitterToken, TwitterTrend
import tweepy

# Create your views here.
def trends(requests):
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
			TwitterTrend(location_id=data['locations'][0]['woeid'], trends=data, location=data['locations'][0]['name'], created_at=dateparse.parse_datetime(data['created_at'])).save()
		except Exception, e:
			context[u'twitter'] = str(e)
		finally:
			context[u'twitter_status'] = u'Retrieve trends from Twitter API and updated database.'
	else:
		context[u'twitter'] = TwitterTrend.objects.filter(location_id=1)[0].trends
		context[u'twitter_status'] = 'Trends retrieved within last 30 minutes. Showing cached result.'
	context['time_taken'] = timezone.now() - start_time
	return render(requests, template, context)