from django.db import models

# Create your models here.


class manage_flower(object):
    def __init__(self, idProduct, nameProduct, expiredProduct, quantityProduct, categoriesCode):
        self.id = idProduct
        self.name = nameProduct
        self.expire = expiredProduct
        self.quantity = quantityProduct
        self.code = categoriesCode


class order(object):
    def __init__(self,idSalesCart, quantityOfProductsSold, PriceOfProductsSold, add):
        self.id_sales_cart = idSalesCart
        self.quantity_product = quantityOfProductsSold
        self.Price_Product = PriceOfProductsSold
        self.address = add


class statistics(object):
    def __init__(self, idSalesCart, quantityOfProductsSold, PriceOfProductsSold, total):
        self.idSalesCarT = idSalesCart
        self.QuantityProducT = quantityOfProductsSold
        self.PriceProducT = PriceOfProductsSold
        self.total = total


class total(object):
    def __init__(self, quantity, totalmoney):
        self.quantity_total = quantity
        self.total_money = totalmoney

