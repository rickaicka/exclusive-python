from email.policy import default

from django.db import models
from django import forms

import logging

logger = logging.getLogger('django')

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Categoria')
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

class ImageCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome', blank=True, default=None, null=True)
    image = models.FileField(upload_to='categories/', verbose_name='Imagem', blank=True, default=None, null=True)
    category = models.OneToOneField('Category', on_delete=models.CASCADE, related_name='image', verbose_name='Categoria', blank=False, default=None, null=False)

    class Meta:
        ordering = ["id", "category", "image"]

    def __str__(self):
        return f'{self.category.name} - {self.image}'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    categories = models.ManyToManyField('Category', related_name='produtos', verbose_name='Categorias')
    rating = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='Avaliação', blank=True, default=None, null=True)
    sizes = models.CharField(max_length=100, verbose_name='Tamanho', blank=True, default=None, null=True)
    colors = models.CharField(max_length=100, verbose_name='Cor', blank=True, default=None, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Desconto', blank=True, default=None, null=True)
    stock_quantity = models.IntegerField(verbose_name="Quantidade em Estoque",  blank=False, default=0, null=False)
    active = models.BooleanField(verbose_name="Produto Ativo", blank=False, default=True, null=False)
    flashSales = models.BooleanField(verbose_name="Promoção de Vendas", blank=False, default=False, null=False)
    bestSelling = models.BooleanField(verbose_name="Destaque de Vendas", blank=False, default=False, null=False)
    highlight = models.BooleanField(verbose_name="Produto de Destaque", blank=False, default=False, null=False)
    isNew = models.BooleanField(verbose_name="Produto Novo", blank=False, default=False, null=False)
    tags = models.ManyToManyField('Tag', related_name='produtos', verbose_name='Tags')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='produtos', verbose_name='Marca', blank=False, default=None, null=False)

    @property
    def images(self):
        return self.imagens.all()

    @property
    def categories_list(self):
        return self.categories.all()

    class Meta:
        ordering = ["id",]

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome', blank=True, default=None, null=True)
    image = models.FileField(upload_to='products/', verbose_name='Imagem', blank=True, default=None, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='imagens', verbose_name='Produto', blank=True, default=None, null=True)
    class Meta:
        ordering = ["id",]

    def __str__(self):
        return f'{self.product.name} - {self.image}'

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(max_length=100, verbose_name='E-mail')
    password = models.CharField(max_length=100, verbose_name='Senha')
    class Meta:
        ordering = ["id",]

    def __str__(self):
        return f'id: {self.id} - nome: {self.name}'

class PaymentInfo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='pagamentos', verbose_name='Usuário')
    card_number = models.CharField(max_length=16, verbose_name='Número do Cartão')
    card_holder = models.CharField(max_length=100, verbose_name='Nome no Cartão')
    card_expiration_date = models.DateField(verbose_name='Data de Validade')
    card_cvv = models.CharField(max_length=3, verbose_name='CVV')
    class Meta:
        ordering = ["id",]

    def __str__(self):
        return f'{self.user.name} - {self.card_number} - {self.card_holder} - {self.card_expiration_date} - {self.card_cvv} '

class BillingInfo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='faturamentos', verbose_name='Usuário')
    address = models.CharField(max_length=100, verbose_name='Endereço')
    complement = models.CharField(max_length=100, verbose_name='Complemento', blank=True)
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=100, verbose_name='Estado')
    zip_code = models.CharField(max_length=8, verbose_name='CEP')
    class Meta:
        ordering = ["id",]

    def __str__(self):
        return f'{self.user.name} - {self.address} - {self.complement} - {self.city} - {self.state} - {self.zip_code} '

class Order(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='pedidos', verbose_name='Usuário')
    products = models.ManyToManyField('Product', related_name='pedidos', verbose_name='Produtos')
    payment_info = models.ForeignKey('PaymentInfo', on_delete=models.CASCADE, related_name='pedidos', verbose_name='Informações de Pagamento')
    billing_info = models.ForeignKey('BillingInfo', on_delete=models.CASCADE, related_name='pedidos', verbose_name='Informações de Faturamento')
    cupom_code = models.CharField(max_length=100, verbose_name='Cupom', blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total')

    class Meta:
        ordering = ["id", ]

    def __str__(self):

        return self.user.name

class WishList(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='wishlists', verbose_name='Usuário')
    products = models.ManyToManyField('Product', related_name='wishlists', verbose_name='Produtos')

    class Meta:
        ordering = ["id", ]

    def __str__(self):
        return self.user.name

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Marca', blank=False, default=None, null=True)
    class Meta:
        ordering = ["id", "name"]

    def __str__(self):
        return f'{self.name} '

class Review(models.Model):
    review_text = models.TextField(max_length=300, verbose_name='Review', blank=False, null=False, default='')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews', verbose_name='Produto', null=True)

    class Meta:
        ordering = ["id", "review_text"]

    def __str__(self):
        return f'{self.review_text}'

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Tag', blank=True, default=None, null=True)
    class Meta:
        ordering = ["id", "name"]

    def __str__(self):
        return f'{self.name} '