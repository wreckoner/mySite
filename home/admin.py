from django.contrib import admin
from .models import HomeInformation

# Register your models here.
class HomeInformationAdmin(admin.ModelAdmin):
	list_display = ('category', 'heading', 'description', 'url', 'start', 'stop')

admin.site.register(HomeInformation, HomeInformationAdmin)