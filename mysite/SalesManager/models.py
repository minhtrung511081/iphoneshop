from django.db import models
from AccountManagement.models import Account
from ProductManager.models import Product
from soft_delete_it.models import SoftDeleteModel
# Create your models here.


class SalesInvoices(SoftDeleteModel):
    idSalesInvoices = models.IntegerField(primary_key=True)
    dateCreateInvoice = models.DateTimeField()
    idAccountCode = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idSalesInvoices)


class SalesCart(SoftDeleteModel):
    idSalesCart = models.IntegerField(primary_key=True)
    quantityOfProductsSold = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    PriceOfProductsSold = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    createdTime = models.DateTimeField()
    updatedTime = models.DateTimeField()
    productCode = models.ForeignKey(Product, on_delete=models.CASCADE)
    salesInvoicesCode = models.ForeignKey(SalesInvoices, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idSalesCart)
