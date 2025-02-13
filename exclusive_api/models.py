from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Categoria')

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    categories = models.ManyToManyField('Category', related_name='produtos', verbose_name='Categorias')
    class Meta:
        ordering = ["id",]

    def __str__(self):
        return self.name

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