from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^parents/$', views.ParentsList.as_view()),
    url(r'^children/$', views.ChildrenList.as_view()),
    url(r'^school/$', views.SchoolList.as_view()),
    url(r'^location/$', views.LocationList.as_view()),
]
