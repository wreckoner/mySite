from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from .models import TwitterToken
import tweepy

# Create your views here.
def trends(requests):
	tokens = TwitterToken.objects.all()[0]

	consumerKey = tokens.consumerKey
	consumerSecret = tokens.consumerSecret
	accessToken = tokens.accessToken
	accessTokenSecret = tokens.accessTokenSecret

	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessTokenSecret)
	api = tweepy.API(auth)
	data = api.trends_place(1)
	return JsonResponse(data, safe=False)