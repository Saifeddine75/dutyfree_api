from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path(settings.BASE_URL + "admin/", admin.site.urls),
    path(settings.BASE_URL + 'v1/', include('purchase.urls')),
]
