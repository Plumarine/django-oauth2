#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

# Core authentication (user, session, etc...)
urlpatterns = patterns('',
    url(r'^authenticate/core/$', 'django_oauth2.authentication.core.handle', name='django_oauth2_authenticate_core'),
)
