from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<data_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^data/today/$', views.today, name='today'),
    url(r'^data/(?P<styear>\d{4})-(?P<stmonth>\d{2})-(?P<stday>\d+)/(?P<edyear>\d{4})-(?P<edmonth>\d{2})-(?P<edday>\d+)/$', views.timeslice, name='timeslice'),
    url(r'^data/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d+)/$', views.day, name='day'),

]
