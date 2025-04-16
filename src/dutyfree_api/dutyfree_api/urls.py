from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', RedirectView.as_view(url='/v1/customers/', permanent=False)),
    # Direct versioned routes
    path('v1/', include('purchase.api.v1.urls')),
]
