from django.core.management.base import BaseCommand
from apps.property.models import Property
from apps.ad.models import Ad
class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(5):
            Property.objects.create(
                code=f'codigo-{i}', 
                max_guests=i+1, 
                num_bathrooms=i+1, 
                pet_friendly=True,
                cleaning_fee = i+1,
                activation_date='2022-01-01'
            )
        
        for i in range(3):
            Ad.objects.create(
                property=Property.objects.first(),
                platform=f'plataforma-{i}',
                platform_fee = i+1,
            )