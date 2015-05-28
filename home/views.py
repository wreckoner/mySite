from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import HomeInformation as db
import random

# Create your views here.

def home(requests):
	template = "home.html"
	context = {'title':'Dibyendu Das'}
	context['heading'] = 'Dibyendu Das'
	context['description'] = "Welcome to my website. You can click on the links above for more information!"
	context['work'] = [{'head':x.heading, 'desc':x.description, 'url':x.url, 'start':x.start, 'stop':x.stop} for x in db.objects.filter(category='WR').order_by('stop').reverse()]
	context['education'] = [{'head':x.heading, 'desc':x.description, 'url':x.url, 'start':x.start, 'stop':x.stop} for x in db.objects.filter(category='ED').order_by('stop').reverse()]
	context['prosearch'] = [{'head':x.heading, 'desc':x.description, 'url':x.url, 'start':x.start, 'stop':x.stop} for x in db.objects.filter(category='PR').order_by('stop').reverse()]
	background_colors = ['darkolivegreen', 'darkslategray', 'firebrick', 'indigo', 'slategray', 'olivedrab', 'teal', 'black', 'steelblue', 'forestgreen', 'darkgoldenrod', 'mediumorchid', 'darkslateblue', 'indianred', 'cornflowerblue']
	context['bgColor'] = random.choice(background_colors)
	return render(requests, template, context)