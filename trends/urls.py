from django.conf.urls import include, url
from .views import trends


urlpatterns = [
	url(r'^$', trends),
]