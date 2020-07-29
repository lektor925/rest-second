from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from product.models import ProductSets, Recipient, Order
from product.serializers import ProductSetsSerializer, RecipientSerializer, OrderSerializer


class PageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 15


class ProductSetsViewset(ReadOnlyModelViewSet):
    queryset = ProductSets.objects.all()
    serializer_class = ProductSetsSerializer
    pagination_class = PageNumberPagination


class RecipientViewset(ReadOnlyModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    pagination_class = PageNumberPagination

    @action(methods=['PATCH'], detail=True)
    def change_recipient(self, request, pk=None):
        recipient = Recipient.objects.get(pk=pk)
        serializer = RecipientSerializer(recipient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewset(UpdateModelMixin, ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order_created_datetime', 'delivery_datetime', 'status']
    pagination_class = PageNumberPagination
