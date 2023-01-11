from django.db import models

class Property(models.Model):
    code = models.CharField(max_length=255)
    max_guests = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    pet_friendly = models.BooleanField()
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)