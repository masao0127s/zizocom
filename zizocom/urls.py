#!/usr/bin/env python
# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
from z_server import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zizocom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^z_server/', include('z_server.urls')),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	# url(r'^', include('django.contrib.staticfiles.urls')),

	# from here, application dependent urls
)
