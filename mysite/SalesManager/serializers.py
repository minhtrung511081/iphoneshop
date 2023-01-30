from rest_framework import serializers
from SalesManager.models import *


class SalesInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoices
        fields = '__all__'


class SalesCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesCart
        fields = '__all__'
