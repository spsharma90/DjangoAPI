from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
from api.serializers import ProductSerializer,OrderSerializer,ProductInfoSerializer
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    # return JsonResponse({
    #     'data' : serializer.data
    # })
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def order_list(request):
    # orders = Order.objects.all()
    # orders = Order.objects.prefetch_related(
    #     'items','items__product'
    # ).all()
    orders = Order.objects.prefetch_related('items__product')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)