
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from exclusive_api.views import (
    CategoryViewSet, ProductViewSet, UserViewSet, PaymentInfoViewSet, WishListViewSet,
    PaymentInfoApi, ImageViewSet, ProductApi, WishListApi, ImageCategoryViewSet, BrandViewSet, BrandApi, ReviewViewSet,
    ReviewApi, TagViewSet, TagApi
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Definindo a visualização da documentação
schema_view = get_schema_view(
   openapi.Info(
      title="API de E-commerce",
      default_version='v1',
      description="Documentação da API de E-commerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@ecommerce.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(IsAuthenticatedOrReadOnly,),
)


# Registrando as rotas da API
router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='Category')
router.register('products', ProductViewSet, basename='Product')
router.register('users', UserViewSet, basename='User')
router.register('images', ImageViewSet, basename='Image')
router.register('category_images', ImageCategoryViewSet, basename='Category Image')
router.register('payment_infos', PaymentInfoViewSet, basename='PaymentInfo')
router.register('wish_list', WishListViewSet, basename='WishList')
router.register('brands_list', BrandViewSet, basename='Brands')
router.register('reviews_list', ReviewViewSet, basename='Reviews')
router.register('tags_list', TagViewSet, basename='Tags')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('payment-infos/', PaymentInfoApi.as_view(), name='payment-infos'),
    path('products/', ProductApi.as_view(), name='products'),
    path('wish-list/', WishListApi.as_view(), name='wish-list'),
    path('brands/', BrandApi.as_view(), name='brands'),
    path('reviews/', ReviewApi.as_view(), name='reviews'),
    path('tags/', TagApi.as_view(), name='tags'),

    # Adicionando a documentação da API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-schema'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
