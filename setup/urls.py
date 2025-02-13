
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from exclusive_api.views import CategoryViewSet, ProductViewSet, UserViewSet, PaymentInfoApi

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='Category')
router.register('products', ProductViewSet, basename='Product')
router.register('users', UserViewSet, basename='User')
# router.register('payment-infos/', PaymentInfoViewSet, basename='PaymentInfo')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('payment-infos/', PaymentInfoApi.as_view(), name='payment-infos'),
]
