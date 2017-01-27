from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListDrivers.as_view()),
    url(r'^vehicle$', views.ListVehicle.as_view()),
]