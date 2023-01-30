from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, permissions
from django.http import HttpResponse
import django_filters.rest_framework
from PurchaseManagement.serializers import *
# Create your views here.


class PurchaseInvoiceList(generics.ListCreateAPIView):
    # queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    pagination_class = LimitOffsetPagination
    # permission_classes = [permissions.AllowAny]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['accountCode', 'sourceInputCode']

    def get_queryset(self):
        if self.request.user.is_staff is True:
            queryset = PurchaseInvoice.objects.all()
        else:
            queryset = PurchaseInvoice.objects.filter(accountCode=self.request.user.id)
        return queryset

    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff is True:
            return self.create(request, *args, **kwargs)
        else:
            return HttpResponse("you not permission create Purchase Invoice")


class DetailedPurchaseInvoice(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = PurchaseInvoiceSerializer
    permission_classes = [permissions.IsAdminUser]


class SourceInputList(generics.ListCreateAPIView):
    queryset = SourceInput.objects.all()
    serializer_class = InputSourceSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['phoneSourceInput', 'emailSourceInput']


class DetailedSourceInput(generics.RetrieveUpdateDestroyAPIView):
    queryset = SourceInput.objects.all()
    serializer_class = InputSourceSerializer
    permission_classes = [permissions.IsAdminUser]


class PurchaseInvoiceDetailsList(generics.ListCreateAPIView):
    queryset = PurchaseInvoiceDetails.objects.all()
    serializer_class = PurchaseInvoiceDetailsSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = LimitOffsetPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['productCode', 'purchaseInvoiceCode']


class DetailedPurchaseInvoiceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseInvoiceDetails.objects.all()
    serializer_class = PurchaseInvoiceDetailsSerializer
    permission_classes = [permissions.IsAdminUser]
