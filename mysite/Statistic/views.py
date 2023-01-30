from Statistic.serializers import *
from rest_framework import generics
from Statistic.models import *
from ProductManager.models import Product
from SalesManager.models import SalesCart
from AccountManagement.models import Account


class manageCategories(generics.ListCreateAPIView):
    serializer_class = managecategories_Serializers

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            queryset = Product.objects.filter(categoriesCode__idCategories=self.request.data.get('categories'))
            result = []
            for i in queryset:
                result.append(manage_flower(i.idProduct, i.nameProduct, i.expiredProduct, i.quantityProduct, i.categoriesCode))
        return result


class order_view(generics.ListCreateAPIView):
    serializer_class = order_Serializers

    def get_queryset(self):
        if self.request.user.is_staff is True:
            card = SalesCart.objects.filter(salesInvoicesCode__idSalesInvoices=self.request.data.get('id_invoice'))

            result = []
            for ca in card:
                account = Account.objects.filter(salesinvoices__idSalesInvoices=self.request.data.get('id_invoice'))
                add = []

                for ac in account:
                    add.append(ac.address)

                result.append(order(ca.idSalesCart, ca.quantityOfProductsSold, ca.PriceOfProductsSold, add))
            return result


class statisticsView(generics.ListCreateAPIView):
    serializer_class = statisticsSerializer

    def get_queryset(self):
        if self.request.user.is_staff is True:
            card = SalesCart.objects.filter(productCode__nameProduct=self.request.data.get('nameCategories'))
            # queryset = Product.objects.filter(categoriesCode__idCategories=self.request.data.get('categories'))
            result = []
            total = 0
            for i in card:
                total = i.quantityOfProductsSold * i.PriceOfProductsSold
                result.append(statistics(i.idSalesCart, i.quantityOfProductsSold, i.PriceOfProductsSold, total))
        return result


class totalView(generics.ListCreateAPIView):
    serializer_class = totalSerializer

    def get_queryset(self):
        if self.request.user.is_staff is True:
            card = SalesCart.objects.filter(productCode__nameProduct=self.request.data.get('nameCategories'))
            result = []
            quantity = 0
            # totalMoney = decimal.Decimal(0.0)
            totalMoney = 0
            for i in card:
                quantity = i.quantityOfProductsSold + quantity
                totalMoney = i.quantityOfProductsSold * i.PriceOfProductsSold + totalMoney
            result.append(total(quantity, totalMoney))
        return result
