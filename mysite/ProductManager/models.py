from django.db import models
from soft_delete_it.models import SoftDeleteModel


class Categories(SoftDeleteModel):
    idCategories = models.IntegerField(primary_key=True)
    nameCategories = models.CharField(max_length=100)

    def __str__(self):
        return self.nameCategories


class Product(SoftDeleteModel):
    idProduct = models.IntegerField(primary_key=True)
    nameProduct = models.CharField(max_length=100)
    expiredProduct = models.DateTimeField()
    quantityProduct = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    categoriesCode = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nameProduct)


