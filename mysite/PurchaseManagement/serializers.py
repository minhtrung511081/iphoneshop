from rest_framework import serializers
from PurchaseManagement.models import *


class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = '__all__'


class PurchaseInvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoiceDetails
        fields = '__all__'


class InputSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceInput
        fields = '__all__'

