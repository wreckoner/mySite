from django.db import models

# Create your models here.

class HomeInformation(models.Model):
	heading = models.CharField(max_length=100, unique=True)
	description = models.TextField(blank=True)
	url = models.URLField(blank=True, null=True)
	start = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	stop = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	CATEGORY_CHOICES = (				#This variable specifies the categories for the links on the toolbar.
		('PR', 'Projects and Research'),
		('ED', 'Education'),
		('WR', 'Work'),
	)
	category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='WR')

	def __repr__(self):
		return u': '.join([self.category, self.heading])