from django.conf.urls import patterns, include, url
from deal.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bowlerdeals.views.home', name='home'),
    # url(r'^bowlerdeals/', include('bowlerdeals.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^deal/(?P<deal_id>\d+)/$', detail),
)


