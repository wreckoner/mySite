from django.db import models

# Create your models here.

class TwitterToken(models.Model):
	consumerKey = models.CharField(primary_key=True, max_length=100)
	consumerSecret = models.CharField(max_length=100)
	accessToken = models.CharField(max_length=100)
	accessTokenSecret = models.CharField(max_length=100)

	def __repr__(self):
		return self.consumerKey