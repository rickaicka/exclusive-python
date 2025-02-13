from rest_framework import viewsets
from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .models import Category, Product, User, PaymentInfo
from .serializers import CategorySerializer, ProductSerializer, UserSerializer, PaymentInfoSerializer
from django.shortcuts import get_object_or_404

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