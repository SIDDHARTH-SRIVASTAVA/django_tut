from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, my_image, hello_pdf
from django.conf.urls.defaults import *
from mysite.feeds import LatestEntries, LatestEntriesByCategory

feeds = {'latest':LatestEntries,
	'categories': LatestEntriesByCategory,
	}

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^hello/$', hello),
    # Examples:
	url(r'^$', 'mysite.views.home', name='home'),
	url(r'^time/	$', current_datetime),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^pic/$', my_image),
	url(r'^pdf/$', hello_pdf),
	url(r'^feeds/(?P<url>.*)/$)', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

)
