from django.conf.urls import url, include
from wishapp import views
urlpatterns = [
    url(r'^dreamers/all/$', views.dreamers),
    url(r'^dreamers/(?P<dreamer_id>\d+)/$', views.dreamer),
    url(r'^create/(?P<user_id>\d+)/', views.dreamer),
    url(r'^dreamers/adddesire/(?P<dreamer_id>\d+)/$', views.adddesire),
    url(r'^$', views.dreamers),

]
