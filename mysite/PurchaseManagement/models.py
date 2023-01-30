from django.db import models
from AccountManagement.models import Account
from ProductManager.models import Product
from soft_delete_it.models import SoftDeleteModel
# Create your models here.


class SourceInput(SoftDeleteModel):
    idSourceInput = models.IntegerField(primary_key=True)
    addressSourceInput = models.CharField(max_length=100)
    emailSourceInput = models.CharField(max_length=45)
    phoneSourceInput = models.CharField(max_length=11)

    def __str__(self):
        return str(self.idSourceInput)


class PurchaseInvoice(SoftDeleteModel):
    idPurchaseInvoice = models.IntegerField(primary_key=True)
    dateCreatePurchaseInvoice = models.DateTimeField()
    accountCode = models.ForeignKey(Account, on_delete=models.CASCADE)
    sourceInputCode = models.ForeignKey(SourceInput, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idPurchaseInvoice)


class PurchaseInvoiceDetails(SoftDeleteModel):
    id = models.IntegerField(primary_key=True)
    productCode = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantityOfPurchasedProducts = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    buyProductPrice = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    purchaseInvoiceCode = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.productCode)
