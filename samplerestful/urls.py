from django.conf.urls import url, include
from django.contrib import admin

from sample_app import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(urls)),
]
