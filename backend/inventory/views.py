from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Stock
from .serializers import CategorySerializer, ProductSerializer, StockSerializer
from .docs import (
    category_list_docs, category_create_docs, category_delete_docs,
    product_list_docs, product_create_docs, product_delete_docs,
    stock_list_docs, stock_update_docs, stock_delete_docs
)
from users.models import UserActivity
from users.permissions import IsSuperAdmin


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']

    @category_list_docs
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @category_create_docs
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            UserActivity.objects.create(
                user=request.user,
                action_type=UserActivity.ActionType.CREATE,
                model_name='Category',
                object_id=response.data['id'],
                details={'name': response.data['name']}
            )
        return response

    @category_delete_docs
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            UserActivity.objects.create(
                user=request.user,
                action_type=UserActivity.ActionType.DELETE,
                model_name='Category',
                object_id=instance.id,
                details={'name': instance.name}
            )
        return response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description', 'sku', 'barcode']
    ordering_fields = ['name', 'price', 'created_at']

    @product_list_docs
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @product_create_docs
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            UserActivity.objects.create(
                user=request.user,
                action_type=UserActivity.ActionType.CREATE,
                model_name='Product',
                object_id=response.data['id'],
                details={'name': response.data['name'],
                         'price': response.data['price']}
            )
        return response

    @product_delete_docs
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            UserActivity.objects.create(
                user=request.user,
                action_type=UserActivity.ActionType.DELETE,
                model_name='Product',
                object_id=instance.id,
                details={'name': instance.name}
            )
        return response

    @action(detail=False, methods=['post'], permission_classes=[IsSuperAdmin])
    def bulk_price_update(self, request):
        """
        Bulk update prices for products across all stores.
        Only accessible by super admin.
        """
        product_id = request.data.get('product_id')
        new_price = request.data.get('new_price')

        if not product_id or not new_price:
            return Response(
                {'error': 'Both product_id and new_price are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
            old_price = product.price
            product.price = new_price
            product.save()

            # Log the price update activity
            UserActivity.objects.create(
                user=request.user,
                action_type=UserActivity.ActionType.PRICE_UPDATE,
                model_name='Product',
                object_id=product.id,
                details={
                    'name': product.name,
                    'old_price': str(old_price),
                    'new_price': str(new_price)
                }
            )

            return Response({
                'message': f'Price updated successfully for {product.name}',
                'old_price': old_price,
                'new_price': new_price
            })
        except Product.DoesNotExist:
            return Response(
                {'error': 'Product not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['product']
    search_fields = ['product__name']
    ordering_fields = ['quantity', 'last_updated']

    @stock_list_docs
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @stock_update_docs
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            instance = self.get_object()
            UserActivity.objects.create(
                user=request.user,
                action_type=UserActivity.ActionType.UPDATE,
                model_name='Stock',
                object_id=instance.id,
                details={
                    'product': instance.product.name,
                    'quantity': instance.quantity
                }
            )
        return response

    @stock_delete_docs
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            UserActivity.objects.create(
                user=request.user,
                action_type=UserActivity.ActionType.DELETE,
                model_name='Stock',
                object_id=instance.id,
                details={'product': instance.product.name}
            )
        return response
