from django.db import models
from apps.property.models import Property


class Ad(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    platform = models.CharField(max_length=255)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
