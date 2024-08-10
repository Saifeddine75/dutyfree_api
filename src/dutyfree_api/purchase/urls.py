from django.urls import path
from purchase.views import CustomerCreateListAPIView

urlpatterns = [
    path('customers/', CustomerCreateListAPIView.as_view(), name='customer-create-list'),
]
