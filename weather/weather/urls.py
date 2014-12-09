from django.conf.urls import patterns, url

from weather import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<node_id>\d+)/$', views.detail, name='detail'),
#                       url(r'^(?P<node_id>\d+)/results/$', views.results, name='results'),
                       url(r'^submit/$', views.submit),
)
