from django.conf.urls import url, include


urlpatterns = [
    url(r'^user/', include('rest_auth.urls')),
]