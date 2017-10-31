from django.conf.urls import url, include
from wishapp import views
urlpatterns = [
    url(r'^dreamers/all/$', views.dreamers),
    url(r'^login1/$', views.login1, name='login1'),
    url(r'^register1/$', views.register1, name='register1'),
    url(r'^dreamers/(?P<dreamer_id>\d+)/$', views.dreamer, name='dreamer'),
    url(r'^dreamers/adddesire/(?P<dreamer_id>\d+)/$', views.adddesire, name='adddesire'),
    url(r'^dreamers/deldesire/(?P<dreamer_id>\d+)/$', views.deldesire, name='deldesire'),
    url(r'^dreamers/editdesire/(?P<dreamer_id>\d+)/(?P<desire_id>\d+)/$', views.editdesire, name='editdesire'),
    url(r'^selectdesire/$', views.selectdesire, name='selectdesire'),
    url(r'^backupdesire/$', views.backupdesire, name='backupdesire'),
    url(r'^dreamers/archive/(?P<user_id>\d+)/$', views.archive, name='archive'),
    url(r'^dreamers/delarchive/(?P<user_id>\d+)/$', views.delarchive, name='delarchive'),
    url(r'^$', views.dreamers),
]
