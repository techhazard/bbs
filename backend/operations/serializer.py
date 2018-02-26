from rest_framework import serializers
from operations.models import Product, Purchase, BBSUser

class BBSUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BBSUser
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
