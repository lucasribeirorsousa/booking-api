from django.db import models
from apps.ad.models import Ad


class Reservation(models.Model):
    code = models.CharField(max_length=255)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField()
    num_guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)