# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from .views import TagDetailView
from .views import TagListView

urlpatterns = patterns('',
    url(r'^$',                  TagListView.as_view(),      name='universaltag-tag-list'),
    url(r'^(?P<slug>[^/]+)/$',  TagDetailView.as_view(),    name='universaltag-tag-detail'),
    url(r'^api/',               include('universaltag.api.urls')),
)
