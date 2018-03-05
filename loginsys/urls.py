from django.conf.urls import url, include
from loginsys.views import logout, register
from wishapp import views
urlpatterns = [
   url(r'^login/', views.login),
   url(r'^logout/', logout),
   url(r'^register/', register),

]
