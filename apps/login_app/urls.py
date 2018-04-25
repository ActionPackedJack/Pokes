from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^Registration$',views.validate),
    url(r'^success$',views.success),
    url(r'^Login$',views.login),
    url(r'^logout$',views.logout),
    url(r'^poke/(?P<id>[0-9]+)$', views.poke),
]