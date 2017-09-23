from django.conf.urls import url, include
from wishapp import views
urlpatterns = [
    url(r'^$', views.dreamers),
    url(r'^dreamers/all/$', views.dreamers),
    url(r'^dreamers/(?P<dreamer_id>\d+)/$', views.dreamer),


]
