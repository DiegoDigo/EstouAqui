from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^', include("Users.urls")),
    url(r'^parents/$', views.ParentsList.as_view()),
    url(r'^children/$', views.ChildrenList.as_view()),
    url(r'^school/$', views.SchoolList.as_view()),
    url(r'^location/$', views.LocationList.as_view()),
    url(r'^drivers/', include('Drives.api.urls')),
]
