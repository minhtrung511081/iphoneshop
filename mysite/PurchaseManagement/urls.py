from django.urls import *
from django.conf.urls import *
from PurchaseManagement import views
urlpatterns = [
    path('PurchaseInvoiceList/', views.PurchaseInvoiceList.as_view()),
    path('DetailedPurchaseInvoice/<int:pk>/', views.DetailedPurchaseInvoice.as_view()),
    path('SourceInputList/', views.SourceInputList.as_view()),
    path('DetailedSourceInput/<int:pk>/', views.DetailedSourceInput.as_view()),
    path('PurchaseInvoiceDetailsList/', views.PurchaseInvoiceDetailsList.as_view()),
    path('DetailedPurchaseInvoiceDetails/<int:pk>/', views.DetailedPurchaseInvoiceDetails.as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
