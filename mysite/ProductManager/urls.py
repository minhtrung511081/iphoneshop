from django.urls import *

from django.conf.urls import *
from ProductManager import views

urlpatterns = [
    path('CategoriesList/', views.CategoriesList.as_view()),
    path('DetailedCategories/<int:pk>/', views.DetailedCategories.as_view()),
    path('ProductList/', views.ProductList.as_view()),
    path('DetailedProduct/<int:pk>/', views.DetailedProduct.as_view()),
]