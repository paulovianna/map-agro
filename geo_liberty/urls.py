from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from views import upload

admin.autodiscover()

urlpatterns = patterns('',
                       
     url(r'^admin/', include(admin.site.urls)),
     url(r'^upload/$',upload),
     url(r'^chaining/', include('smart_selects.urls')),
     url(r'^mapagro/', include('mapagro.urls')),
     # Required to make static serving work 
     url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
