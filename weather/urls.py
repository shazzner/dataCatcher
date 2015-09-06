from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<data_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^data/(?P<styear>\d{4})-(?P<stmonth>\d{2})-(?P<stday>\d+)/(?P<edyear>\d{4})-(?P<edmonth>\d{2})-(?P<edday>\d+)/$', views.timeslice, name='timeslice'),

]
