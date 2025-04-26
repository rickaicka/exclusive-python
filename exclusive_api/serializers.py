from rest_framework import serializers
from .models import Category, Product, User, PaymentInfo, Image, WishList, ImageCategory, Brand, Review, Tag
import logging
logger = logging.getLogger('django')

class BaseModelSerializer(serializers.ModelSerializer):
    """
    Serializer base que adiciona automaticamente placeholders
    usando os verbose_name dos campos do model.
    Também adiciona autofocus no primeiro campo editável.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        first = True
        for field_name, field in self.fields.items():
            if hasattr(field, 'style') and field.read_only is False:
                try:
                    model_field = self.Meta.model._meta.get_field(field_name)
                    placeholder = model_field.verbose_name.capitalize()

                    field.style.update({
                        'placeholder': placeholder
                    })
                    if first:
                        field.style['autofocus'] = True
                        first = False
                except Exception:
                    pass

class ReviewSerializer(BaseModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class BrandSerializer(BaseModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ImageCategorySerializer(BaseModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ImageCategory
        fields = ('id', 'name', 'image', 'image_url', 'category')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

class CategorySerializer(BaseModelSerializer):
    image = ImageCategorySerializer(read_only=True)
    upload_image = serializers.FileField(
        max_length=100000, allow_empty_file=False, use_url=False, write_only=True, required=False
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'upload_image')

    def create(self, validated_data):
        upload_image = validated_data.pop('upload_image', None)
        category = Category.objects.create(**validated_data)

        if upload_image:
            ImageCategory.objects.create(category=category, image=upload_image)

        return category

    def update(self, instance, validated_data):
        upload_image = validated_data.pop('upload_image', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if upload_image:
            if hasattr(instance, 'image'):
                instance.image.image = upload_image
                instance.image.save()
            else:
                ImageCategory.objects.create(category=instance, image=upload_image)

        return instance

class ImageSerializer(BaseModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class TagSerializer(BaseModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProductSerializer(BaseModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all()
    )
    images = ImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    upload_images = serializers.ListField(
        child=serializers.FileField(max_length=100000, allow_empty_file=True, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'price', 'categories', 'rating', 'sizes', 'colors',
            'images', 'upload_images', 'brand', 'stock_quantity',
            'reviews', 'tags', 'discount', 'flashSales', 'bestSelling', 'highlight', 'active', 'isNew'
        )

    def create(self, validated_data):
        upload_images = validated_data.pop('upload_images', [])
        categories = validated_data.pop('categories', [])
        tags = validated_data.pop('tags', [])

        product = Product.objects.create(**validated_data)

        product.categories.set(categories)
        product.tags.set(tags)

        for image in upload_images:
            Image.objects.create(product=product, image=image)

        return product

    def update(self, instance, validated_data):
        upload_images = validated_data.pop('upload_images', [])
        categories = validated_data.pop('categories', None)
        tags = validated_data.pop('tags', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if categories is not None:
            instance.categories.set(categories)
        if tags is not None:
            instance.tags.set(tags)

        for image in upload_images:
            Image.objects.create(product=instance, image=image)

        return instance

class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PaymentInfoSerializer(BaseModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PaymentInfo
        fields = '__all__'

class WishListSerializer(BaseModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = WishList
        fields = '__all__'