from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Categoria')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    categories = models.ManyToManyField('Category', related_name='produtos', verbose_name='Categorias')
    class Meta:
        ordering = ["name",]

    def __str__(self):
        return self.name