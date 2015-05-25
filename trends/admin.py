from django.contrib import admin
from .models import TwitterToken
# Register your models here.

class TwitterTokenAdmin(admin.ModelAdmin):
	list_display = ('consumerKey', 'consumerSecret')

admin.site.register(TwitterToken, TwitterTokenAdmin)