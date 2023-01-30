from django.db import models
from django.contrib.auth.models import AbstractUser
# from authemail.models import EmailAbstractUser, EmailUserManager

# Create your models here.


class Account(AbstractUser):
    phone = models.CharField(max_length=11, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    # date_of_birth = models.DateTimeField('Date of birth', null=True, blank=True)
    # objects = EmailUserManager()

    def __str__(self):
        return self.username