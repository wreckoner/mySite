from django.contrib import admin
from .models import TwitterToken, TwitterTrend
# Register your models here.

class TwitterTokenAdmin(admin.ModelAdmin):
	list_display = ('consumerKey', 'consumerSecret')

class TwitterTrendAdmin(admin.ModelAdmin):
	list_display = ('location_id', 'trends', 'location', 'created_at')

admin.site.register(TwitterToken, TwitterTokenAdmin)
admin.site.register(TwitterTrend, TwitterTrendAdmin)