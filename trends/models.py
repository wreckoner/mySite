from django.db import models

# Create your models here.

class TwitterToken(models.Model):
	consumerKey = models.CharField(primary_key=True, max_length=100)
	consumerSecret = models.CharField(max_length=100)
	accessToken = models.CharField(max_length=100)
	accessTokenSecret = models.CharField(max_length=100)

	def __repr__(self):
		return self.consumerKey


class TwitterTrend(models.Model):
	location_id = models.IntegerField(primary_key=True)
	trends = models.TextField(blank = False)
	location = models.CharField(max_length=50, blank=False)
	created_at = models.DateTimeField(null=False, blank=False)

	def __repr__(self):
		return ' - '.join(map(str, [self.location_id, self.created_at, self.location]))

class TwitterAvailableWoeid(models.Model):
	woeid = models.IntegerField(primary_key=True)
	created_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return ' - '.join(map(str, [self.woeid, self.created_at]))