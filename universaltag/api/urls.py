# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from piston.resource import Resource
from piston.doc import documentation_view

from handlers import TaggedItemHandler

tagged_item_handler = Resource(TaggedItemHandler)

urlpatterns = patterns('',
    url(r'^(?P<content_type>\d+)/(?P<object_id>\d+)/$',                     tagged_item_handler,    name='universaltag-api'),
    url(r'^(?P<content_type>\d+)/(?P<object_id>\d+)/(?P<label>[^/]+)/$',    tagged_item_handler,    name='universaltag-api'),

    # Documentation
    url(r'^doc/$',  documentation_view),
)
