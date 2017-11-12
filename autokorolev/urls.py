#-*- coding: utf-8 -*-

from django.http import HttpResponse
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from auto.views import *

urlpatterns = [
    url(r'^adminka/', admin.site.urls),
    url(r'^$', main_view),
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", content_type="text/plain")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
