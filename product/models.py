from django.db import models


class ProductSets(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)


class Recipient(models.Model):
    surname = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    patronymic = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=15, blank=True)


class Order(models.Model):
    STATUS = (
        ('created', 'created'),
        ('delivered', 'delivered'),
        ('processed', 'processed'),
        ('cancelled', 'cancelled')
    )
    order_created_datetime = models.DateTimeField(auto_now_add=True)
    delivery_datetime = models.DateTimeField(blank=True)
    delivery_address = models.CharField(max_length=255, blank=True)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, related_name='recipient')
    product_set = models.ForeignKey(ProductSets, on_delete=models.CASCADE, related_name='productset')
    status = models.CharField(max_length=30, choices=STATUS)
