"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from rest_framework import routers

from operations import views

router = routers.DefaultRouter()


router.register('product', views.ProductViewSet, base_name='product')
router.register('purchase', views.PurchaseViewSet, base_name='purchase')
router.register('user', views.BBSUserViewSet, base_name='user')

router.register('allpurchases', views.AllPurchaseViewSet, base_name='allpurchases')

urlpatterns = [
#    path('', RedirectView.as_view(url='/api'), name='redirect'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
