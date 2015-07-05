import traceback

from django.shortcuts import render
from django.http import JsonResponse
import tweepy

from .models import TwitterToken


def trends(request):
	template = 'trends.html'
	context = {u'title' : u'Social Network Trends'}
	return render(request, template, context)


def twitter_trends_closest(request):
	u'''API for getting a list of closest WOEIDS for which trends are available. Requires a latitude and longitude.
		Passed as lat and lng in GET request. Queries to Twitter API rate limited to 15 per 15 minute.'''
	lat, lng = request.GET[u'lat'], request.GET[u'lng']
	context = {}
	tokens = TwitterToken.objects.all()[0]
	auth = tweepy.OAuthHandler(consumer_key=tokens.consumerKey, consumer_secret=tokens.consumerSecret)
	auth.set_access_token(key=tokens.accessToken, secret=tokens.accessTokenSecret)
	api = tweepy.API(auth_handler=auth)
	try:
		nearest = api.trends_closest(lat, lng)[0]
		context[u'trends'] = api.trends_place(int(nearest[u'woeid']))[0]
	except Exception as e:
		context[u'success'] = False
		context[u'message'] = u'. '.join([str(e), traceback.format_exc()])
	else:
		context[u'success'] = True
		context[u'message'] = u'Successfully retrieved trends of closest location.'
	return JsonResponse(context)