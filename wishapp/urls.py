from django.conf.urls import url, include
from wishlist import settings
from django.views import static
from wishapp import views
urlpatterns = [
    url(r'^dreamers/all/$', views.dreamers),
    url(r'^order/$', views.order),
    url(r'^dreamers/sort/(?P<sub_id>\w+)/$', views.sort),
    url(r'^dreamers/(?P<sub_id>\w+)/$', views.dreamer, name='dreamer'),
    url(r'^desirelist/$', views.desirelist, name='desirelist'),
    url(r'^adddesirelist/$', views.adddesirelist, name='adddesirelist'),
    url(r'^editdesirelist/$', views.editdesirelist, name='editdesirelist'),
    url(r'^dreamers/adddesire/(?P<sub_id>\w+)/$', views.adddesire, name='adddesire'),

   
    url(r'^dreamers/delarchive/(?P<sub_id>\w+)/$', views.delarchive, name='delarchive'),
    url(r'^dreamers/del_sort_desire/(?P<sub_id>\w+)/$', views.del_sort_desire, name='del_sort_desire'),
    url(r'^dreamers/deldesirelist/(?P<user_id>\w+)/$', views.deldesirelist, name='deldesirelist'),

    url(r'^dreamers/editdesire/(?P<sub_id>\w+)/$', views.editdesire, name='editdesire'),
    url(r'^selectdesire/$', views.selectdesire, name='selectdesire'),
    url(r'^backupdesire/$', views.backupdesire, name='backupdesire'),
    url(r'^dreamers/archive/(?P<sub_id>\w+)/$', views.archive, name='archive'),

    url(r'^dreamers/returnfromarchive/(?P<sub_id>\w+)/$', views.returnfromarchive, name='returnfromarchive'),


    url(r'^uploads/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', views.index),
]
