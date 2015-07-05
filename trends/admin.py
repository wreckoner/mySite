from django.contrib import admin
from .models import TwitterToken, TwitterTrend
# Register your models here.

class TwitterTokenAdmin(admin.ModelAdmin):
	list_display = (u'consumerKey', u'consumerSecret')

class TwitterTrendAdmin(admin.ModelAdmin):
	list_display = (u'location_id', u'trends', u'location', u'created_at')

admin.site.register(TwitterToken, TwitterTokenAdmin)
admin.site.register(TwitterTrend, TwitterTrendAdmin)