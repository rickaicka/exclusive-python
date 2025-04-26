from django.contrib import admin
from .models import Category, Product, User, PaymentInfo, Image, WishList, ImageCategory, Brand, Review, Tag


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
    list_display = ('id','name', 'description', 'price', 'sizes', 'colors', 'discount', 'brand', 'get_category', 'get_images_by_product', 'stock_quantity', 'get_reviews', 'get_tags', 'flashSales', 'bestSelling', 'highlight', 'active', 'isNew')

    def get_category(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

    def get_images_by_product(self, obj):
        images = Image.objects.filter(product=obj.id)
        return ", ".join([image.image.name for image in images])

    def get_reviews(self, obj):
        return ", ".join([review.review_text for review in obj.reviews.all()])

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    get_category.short_description = 'Categorias'
    get_category.admin_order_field = 'categories'
    get_images_by_product.short_description = 'Imagens'
    get_images_by_product.admin_order_field = 'images'
    get_reviews.short_description = 'Reviews'
    get_reviews.admin_order_field = 'reviews'
    get_tags.short_description = 'Tags'
    get_tags.admin_order_field = 'tags'
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

class Brands(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 20
admin.site.register(Brand, Brands)

class Reviews(admin.ModelAdmin):
    list_display = ('id', 'review_text')
    list_display_links = ('id', 'review_text')
    list_per_page = 20
admin.site.register(Review, Reviews)

class Tags(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_per_page = 20
admin.site.register(Tag, Tags)