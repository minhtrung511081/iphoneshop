from django.urls import *
from SalesManager import views
urlpatterns = [
    path('SalesCartList/', views.SalesCartList.as_view()),
    path('DetailedSalesCart/<int:pk>/', views.DetailedSalesCart.as_view()),
    path('SalesInvoicesList/', views.SalesInvoicesList.as_view()),
    path('DetailedSalesInvoices/<int:pk>/', views.DetailedSalesInvoices.as_view()),
]