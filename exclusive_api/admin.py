from itertools import product

from django.contrib import admin
from unicodedata import category
from .models import Category, Product, User, PaymentInfo, Image, WishList, ImageCategory


class Categories(admin.ModelAdmin):
    list_display = ('id','name', 'get_images_by_category')
    def get_images_by_category(self, obj):
        image = ImageCategory.objects.filter(category=obj.id)
        return ", ".join([image.image.name for image in image])
    get_images_by_category.short_description = 'Imagens'
    get_images_by_category.admin_order_field = 'images'
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category',)
    list_per_page = 20
admin.site.register(Category, Categories)

class ImagesCategory(admin.ModelAdmin):
    list_display = ('id','name', 'image')
    list_display_links = ('id', 'name', 'image')
    search_fields = ('name', 'image')
    list_per_page = 20
admin.site.register(ImageCategory, ImagesCategory)

class Images(admin.ModelAdmin):
    list_display = ('id','name', 'image')
    list_display_links = ('id', 'name', 'image')
    search_fields = ('name', 'image')
    list_per_page = 20
admin.site.register(Image, Images)

class Products(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'price', 'get_category', 'get_images_by_product')
    def get_category(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    def get_images_by_product(self, obj):
        images = Image.objects.filter(product=obj.id)
        return ", ".join([image.image.name for image in images])

    get_category.short_description = 'Categorias'
    get_category.admin_order_field = 'categories'
    get_images_by_product.short_description = 'Imagens'
    get_images_by_product.admin_order_field = 'images'
    list_display_links = ('id', 'name', )
    search_fields = ('name', 'description', 'price')
    list_per_page = 20
admin.site.register(Product, Products)

class Users(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'password')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'password')
    list_per_page = 20
admin.site.register(User, Users)

class PaymentInfos(admin.ModelAdmin):
    list_display = ('id','user', 'card_number', 'card_holder', 'card_expiration_date', 'card_cvv')
    list_display_links = ('id', 'user', 'card_number')
    search_fields = ('user', 'card_number', 'card_holder', 'card_expiration_date', 'card_cvv')
    list_per_page = 20
admin.site.register(PaymentInfo, PaymentInfos)

class WishLists(admin.ModelAdmin):
    def get_wishlist(self, obj):
        prod = Product.objects.filter(wishlists=obj.id)
        return ", ".join([product.name for product in prod])

    get_wishlist.short_description = 'Produtos'
    get_wishlist.admin_order_field = 'product'

    list_display = ('id', 'user', 'get_wishlist')
    list_display_links = ('id', 'user', 'get_wishlist')
    search_fields = ('product',)
    list_per_page = 20
admin.site.register(WishList, WishLists)