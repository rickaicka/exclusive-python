from django.contrib import admin
from unicodedata import category
from .models import Category, Product


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