from django.conf.urls import url, include
from wishapp import views
urlpatterns = [
    url(r'^1', views.desire),


]
