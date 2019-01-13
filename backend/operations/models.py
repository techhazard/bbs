from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid


class BBSUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birthdate = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    default_account = models.ForeignKey('Account', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.username)[:8]



class CommonModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.uuid)[:8]

    class Meta:
        abstract = True


class Account(CommonModel):
    owned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256, null=True)


class Product(CommonModel):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=256)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    comment = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)


class Transaction(CommonModel):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    affected_account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    account_balance_pre = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_balance_post = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=256)


class Purchase(CommonModel):
    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.DO_NOTHING)

    # price of product at purchase time
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    # amount of product purchased
    product_amount = models.IntegerField(default=1)

    # amount x price
    product_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=True)
