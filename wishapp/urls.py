from django.conf.urls import url, include
from wishapp import views
urlpatterns = [
    url(r'^dreamers/all/$', views.dreamers),
    url(r'^login1/$', views.login1, name='login1'),
    url(r'^dreamers/(?P<dreamer_id>\d+)/$', views.dreamer, name='dreamer'),
    url(r'^dreamers/adddesire/(?P<dreamer_id>\d+)/$', views.adddesire, name='adddesire'),
    url(r'^dreamers/deldesire/(?P<dreamer_id>\d+)/$', views.deldesire, name='deldesire'),
    url(r'^dreamers/editdesire/(?P<dreamer_id>\d+)/(?P<desire_id>\d+)/$', views.editdesire, name='editdesire'),
    url(r'^dreamers/selectdesire/(?P<dreamer_id>\d+)/(?P<desire_id>\d+)/$', views.selectdesire, name='selectdesire'),
    url(r'^$', views.dreamers),
]
