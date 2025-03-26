from rest_framework import serializers
from .models import Category, Product, User, PaymentInfo, Image, WishList, ImageCategory
import logging

logger = logging.getLogger(__name__)

class ImageCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    image = ImageCategorySerializer(many=False, read_only=True)
    upload_image = serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False),
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        upload_image = validated_data.pop('upload_image')
        category = Category.objects.create(**validated_data)
        for category in upload_images:
            ImageCategory.objects.create(category=category, image=image)
        return category

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    upload_images = serializers.ListField(
        child = serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'categories', 'rating', 'size', 'color', 'images', 'upload_images')

    def create(self, validated_data):
        upload_images = validated_data.pop('upload_images')
        product = Product.objects.create(**validated_data)
        for image in upload_images:
            Image.objects.create(product=product, image=image)
        return product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PaymentInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PaymentInfo
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'