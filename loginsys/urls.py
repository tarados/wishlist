from django.conf.urls import url, include
from loginsys.views import logout, register, login, login_vk

urlpatterns = [
   url(r'^login/', login),
   url(r'^login_vk/', login_vk),
   url(r'^logout/', logout),
   url(r'^register/', register),

]
