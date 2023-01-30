from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('ProductManager.urls')),
    path('account/', include('AccountManagement.urls')),
    path('sales/', include('SalesManager.urls')),
    path('purchase/', include('PurchaseManagement.urls')),
    path('statistic/', include('Statistic.urls')),
]
