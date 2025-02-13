
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from exclusive_api.views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='Category')
router.register('products', ProductViewSet, basename='Product')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
