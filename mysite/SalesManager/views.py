import django_filters.rest_framework
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.pagination import LimitOffsetPagination
from SalesManager.serializers import *
from SalesManager.models import *


class SalesInvoicesList(generics.ListCreateAPIView):
    serializer_class = SalesInvoicesSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['idSalesInvoices', 'idAccountCode']

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return SalesInvoices.objects.all()
        else:
            queryset = SalesInvoices.objects.filter(idAccountCode=self.request.user.id)
            return queryset


class DetailedSalesInvoices(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesInvoices.objects.all()
    serializer_class = SalesInvoicesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser is True:
            return self.update(request, *args, **kwargs)
        else:
            return HttpResponse("you not permission edit sales invoices")

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_staff is True:
            return self.destroy(request, *args, **kwargs)
        else:
            return HttpResponse("you not permission delete sales invoices")


class SalesCartList(generics.ListCreateAPIView):
    serializer_class = SalesCartSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['productCode', 'salesInvoicesCode']

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return SalesCart.objects.all()
        else:
            queryset = SalesCart.objects.filter(salesInvoicesCode__idAccountCode__id=self.request.user.id)
            return queryset


class DetailedSalesCart(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesCart.objects.all()
    serializer_class = SalesCartSerializer
    permission_classes = [permissions.IsAuthenticated]
