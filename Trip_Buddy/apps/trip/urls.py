from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/(?P<num>\d+)/update', views.update),
    url(r'^/(?P<num>\d+)/edit_trip', views.edit_trip),
    url(r'^/(?P<num>\d+)/destroy', views.destroy),
    url(r'^/(?P<num>\d+)/leave', views.leave),
    url(r'^/(?P<num>\d+)/join', views.join),
    url(r'^/(?P<num>\d+)$', views.view_trip),
    url(r'^/create', views.create),
    url(r'^/new_trips', views.new_trips),
    url(r'^$', views.trips),
]