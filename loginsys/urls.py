from django.conf.urls import url, include
from loginsys.views import logout, register, login

urlpatterns = [
   url(r'^login/', login),
   url(r'^logout/', logout),
   url(r'^register/', register),

]
