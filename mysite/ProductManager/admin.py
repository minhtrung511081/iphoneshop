from django.contrib import admin

# Register your models here.
from ProductManager.models import *

admin.site.register(Product),
admin.site.register(Categories),