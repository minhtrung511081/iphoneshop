import django_filters.rest_framework
from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.pagination import LimitOffsetPagination

from ProductManager.models import *
from ProductManager.serializers import *
# Create your views here.


class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['nameCategories']

    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff is True:
            return self.create(request, *args, **kwargs)
        else:
            return HttpResponse("you not permissions create")


class DetailedCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = [permissions.IsAdminUser]


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['nameProduct', 'categoriesCode']

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser is True:
            return self.create(request, *args, **kwargs)
        else:
            return HttpResponse("you not permissions create product")


class DetailedProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser is True:
            return self.update(request, *args, **kwargs)
        else:
            return HttpResponse("you not permission edit product")

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_staff is True:
            return self.destroy(request, *args, **kwargs)
        else:
            return HttpResponse("you not permission delete product")

