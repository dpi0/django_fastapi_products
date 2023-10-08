from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, User
from .serializers import ProductSerializer, UserSerializer
from .producer import publish


class ProductViewSet(viewsets.ModelViewSet):
    def get_all_products(self, request):
        products = Product.objects.all()  # get all from db
        serizalizer = ProductSerializer(
            products, many=True
        )  # serialize them
        return Response(serizalizer.data)  # send the seralized data

    def create_product(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_created", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_product(self, request, product_id=None):
        product = Product.objects.get(id=product_id)
        partial = True
        serializer = ProductSerializer(
            instance=product, data=request.data, partial=partial
        )
        # NOTE: instance=product makes sure that we "update" only the product we got
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_updated", serializer.data)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete_product(self, request, product_id=None):
        product = Product.objects.get(id=product_id)
        product.delete()
        publish("product_deleted", product_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_product(self, request, product_id=None):
        product = Product.objects.get(
            id=product_id
        )  # get the single product
        serializer = ProductSerializer(product)  # serialize it
        return Response(
            serializer.data, status=status.HTTP_200_OK
        )  # send the seralized data


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()  # get all from db
        serializer = UserSerializer(users, many=True)  # serialize them
        return Response(serializer.data)  # send the seralized data

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
