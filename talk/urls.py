"""talk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from words.views import ask_respond, answer_respond, watcher

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^ask/$', ask_respond, name='ask'),
	url(r'^answer/(?P<q_id>\d+)/$', answer_respond, name="answer"),
	url(r'^answer/watch/$', watcher),
]
