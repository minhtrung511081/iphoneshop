from rest_framework import serializers


class managecategories_Serializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=60)
    expire = serializers.DateTimeField()
    quantity = serializers.IntegerField()
    code = serializers.CharField()


class order_Serializers(serializers.Serializer):
    id_sales_cart = serializers.IntegerField()
    quantity_product= serializers.IntegerField()
    Price_Product = serializers.CharField()
    address = serializers.CharField()


class statisticsSerializer(serializers.Serializer):
    idSalesCarT = serializers.IntegerField()
    QuantityProducT = serializers.DecimalField(max_digits=5, decimal_places=2)
    PriceProducT = serializers.DecimalField(max_digits=5, decimal_places=2)
    total = serializers.DecimalField(max_digits=5, decimal_places=2)


class totalSerializer(serializers.Serializer):
    quantity_total = serializers.DecimalField(max_digits=5, decimal_places=2)
    total_money = serializers.DecimalField(max_digits=5, decimal_places=2)