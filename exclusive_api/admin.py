from django.contrib import admin
from unicodedata import category
from .models import Category, Product, User, PaymentInfo


class Categories(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'products',)
    list_per_page = 20
admin.site.register(Category, Categories)

class Products(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'price', 'get_category')
    def get_category(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_category.short_description = 'Categorias'
    get_category.admin_order_field = 'categories'
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