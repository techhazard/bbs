from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from operations import models
from operations import serializer


@permission_classes((TokenHasReadWriteScope,))
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ProductSerializer

    def get_queryset(self):
        return models.Product.objects.all()


class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.PurchaseSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Purchase.objects.filter(user_id=user).order_by('-created')


@permission_classes((IsAdminUser,))
class BBSUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = serializer.BBSUserSerializer

    def get_queryset(self):
        return models.BBSUser.objects.all().order_by('-created')


@permission_classes((IsAdminUser,))
class AllPurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.PurchaseSerializer

    def get_queryset(self):
        return models.Purchase.objects.all().order_by('-created')

def test(request):
    print('called test')
    return HttpResponse(str(request.__dict__))
