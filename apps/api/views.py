from rest_framework.response import Response
from rest_framework.views import APIView

from apps.myapp.models import Product
from apps.api.serializers.product_serializer import ProductSerializer


class ProductList(APIView):
    def get(self, request, format=None):
        all_products = Product.objects.all()
        serialize = ProductSerializer(all_products, many=True)
        return Response(serialize.data)
