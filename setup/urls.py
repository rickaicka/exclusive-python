
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from exclusive_api.views import (
    CategoryViewSet, ProductViewSet, UserViewSet, PaymentInfoViewSet, WishListViewSet,
    PaymentInfoApi, ImageViewSet, ProductApi, WishListApi,
    update
)

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='Category')
router.register('products', ProductViewSet, basename='Product')
router.register('users', UserViewSet, basename='User')
router.register('images', ImageViewSet, basename='Image')
#router.register('payment_infos/', PaymentInfoViewSet, basename='PaymentInfo')

router.register('wish_list', WishListViewSet, basename='WishList')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('payment-infos/', PaymentInfoApi.as_view(), name='payment-infos'),
    path('products/', ProductApi.as_view(), name='products'),
    path('wish-list/', WishListApi.as_view(), name='wish-list'),
    path("update_server/", update, name="update"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
