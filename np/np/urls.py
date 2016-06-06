from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('newspaper.urls')),
]
