#!/usr/bin/env python
# coding: utf-8
from django.conf.urls import patterns, include, url
from z_server import views
from views import *

# top_page = "/services/z_server/home"

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'zizocom.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'getmsg', getmsg, name=getmsg),
	url(r'sendmsg', sendmsg, name=sendmsg)
)
