from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailViewSet, invoice_list

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoice_details', InvoiceDetailViewSet)

urlpatterns = [
    # path('invoices/', invoice_list, name='invoice_list'),
    path('', include(router.urls)),
]
