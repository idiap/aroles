from django.conf.urls import patterns, include, url
from django.conf import settings
#from django.contrib import admin
#from django.conf.urls.static import static
from views.acm_challenge_demo import get_segmented_videos

urlpatterns = patterns('',
	url(r'^$', get_segmented_videos),
	url(r'/(?P<central_video_input_id>\d+)/seek/(?P<chosen_segment_id>\d+)', get_segmented_videos),
	url(r'/(?P<central_video_input_id>\d+)', get_segmented_videos),
)

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()
if 'dajaxice' in settings.INSTALLED_APPS:
	urlpatterns += patterns('',
		url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
	)
