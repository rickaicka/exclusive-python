from django.http import HttpResponse
from gc import get_objects
from itertools import product

from rest_framework import viewsets, generics
from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Category, Product, User, PaymentInfo, Image, WishList
from .serializers import CategorySerializer, ProductSerializer, UserSerializer, PaymentInfoSerializer, ImageSerializer, WishListSerializer
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from git import Repo

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = Repo("https://github.com/rickaicka/exclusive-python")
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
#VIEWSET ROUTES

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PaymentInfoViewSet(viewsets.ModelViewSet):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

#API ROUTES

class PaymentInfoApi(APIView):
    def get(self, request):
        payment_infos = PaymentInfo.objects.all()
        serializer = PaymentInfoSerializer(payment_infos, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        user = get_object_or_404(User, id=request.data['user_id'])
        serializer = PaymentInfoSerializer(data=request.data)
        if serializer.is_valid():
            payment_info = PaymentInfo(
                card_number=serializer.validated_data.get('card_number'),
                card_holder=serializer.validated_data.get('card_holder'),
                card_cvv=serializer.validated_data.get('card_cvv'),
                card_expiration_date=serializer.validated_data.get('card_expiration_date'),
                user=user
            )
            payment_info.save()
            payment_info_serializer = PaymentInfoSerializer(payment_info, many=False)
            return Response(payment_info_serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ImageApi(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        product = get_object_or_404(Product, id=request.data['product_id'])
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = Image(
                name=serializer.validated_data.get('name'),
                image=serializer.validated_data.get('image'),
                url=serializer.validated_data.get('url'),
                product=product
            )
            image.save()
            image_serializer = ImageSerializer(image, many=False)
            return Response(image_serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ProductApi(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product(
                name=serializer.validated_data.get('name'),
                description=serializer.validated_data.get('description'),
                price=serializer.validated_data.get('price'),
                rating=serializer.validated_data.get('rating'),
                size=serializer.validated_data.get('size'),
                color=serializer.validated_data.get('color'),
            )
            product.save()
            product_serializer = ProductSerializer(product, many=False)
            return Response(product_serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class WishListApi(APIView):
    def get(self, request):
        wishlists = WishList.objects.all()
        serializer = WishListSerializer(wishlists, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        user = get_object_or_404(User, id=request.data['user_id'])
        serializer = WishListSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = WishList(
                user=user,
            )
            wishlist.save()
            wishlist_serializer = WishListSerializer(wishlist, many=False)
            wishlist.products.set(request.data['products'])
            for pd in request.data['products']:
                product = get_object_or_404(Product, id=pd)
                wishlist_serializer.data['products'].append(ProductSerializer(product).data)
                prods=[]
                for wls in wishlist_serializer.data['products']:
                    if not isinstance(wls, int):
                        prods.append(wls)
                    else:
                        wishlist_serializer.data['products'].remove(wls)
            wishlist_serializer.data['products'] = prods
            return Response(wishlist_serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)