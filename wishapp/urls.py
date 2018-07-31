from django.conf.urls import url, include
from wishlist import settings
from django.views import static
from wishapp import views
urlpatterns = [
    url(r'^dreamers/all/$', views.dreamers),
    url(r'^order/$', views.order),
    url(r'^dreamers/sort/(?P<dreamer_id>\d+)/(?P<desirelist_id>\d+)/$', views.sort),
    url(r'^dreamers/(?P<dreamer_id>\d+)/(?P<desirelist_id>\d+)/$', views.dreamer, name='dreamer'),
    url(r'^desirelist/(?P<dreamer_id>\d+)/$', views.desirelist, name='desirelist'),
    url(r'^adddesirelist/(?P<dreamer_id>\d+)/$', views.adddesirelist, name='adddesirelist'),
    url(r'^dreamers/adddesire/(?P<dreamer_id>\d+)/(?P<desirelist_id>\d+)/$', views.adddesire, name='adddesire'),
    url(r'^dreamers/deldesire/(?P<dreamer_id>\d+)/$', views.deldesire, name='deldesire'),
    url(r'^dreamers/editdesire/$', views.editdesire, name='editdesire'),
    url(r'^selectdesire/$', views.selectdesire, name='selectdesire'),
    url(r'^backupdesire/$', views.backupdesire, name='backupdesire'),
    url(r'^dreamers/archive/(?P<dreamer_id>\d+)/(?P<desirelist_id>\d+)/$', views.archive, name='archive'),
    url(r'^dreamers/delarchive/(?P<user_id>\d+)/$', views.delarchive, name='delarchive'),
    url(r'^dreamers/returnfromarchive/(?P<user_id>\d+)/$', views.returnfromarchive, name='returnfromarchive'),
    url(r'^dreamers/del_sort_desire/(?P<user_id>\d+)/$', views.del_sort_desire, name='del_sort_desire'),
    url(r'^dreamers/deldesirelist/(?P<user_id>\d+)/$', views.deldesirelist, name='deldesirelist'),
    url(r'^uploads/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', views.dreamers),
]
