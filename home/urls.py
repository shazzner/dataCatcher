from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listings/', views.listings, name='listings'),
    url(r'^about/', views.about, name='about'),
    url(r'^help/', views.about, name='help'),
    url(r'^contribute/', views.about, name='contribute'),
]
