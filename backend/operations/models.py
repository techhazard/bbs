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


class Product(CommonModel):
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=256)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    comment = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)

class Purchase(CommonModel):
    product_id = models.ForeignKey(Product, related_name='product', on_delete=models.DO_NOTHING)
    product_price = models.IntegerField()
    product_amount = models.IntegerField()
    
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING) 
    purchase_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
