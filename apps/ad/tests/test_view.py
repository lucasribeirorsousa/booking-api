from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from apps.ad.models import Ad
from apps.property.models import Property
from apps.ad.serializers import AdSerializer
from apps.ad.views import AdViewSet

class AdViewSetTestCase(TestCase):
    def setUp(self):
        self.property = Property.objects.create(
            code="property1", max_guests=2, num_bathrooms=1,
            pet_friendly=True, cleaning_fee=50.00, activation_date="2022-01-01"
        )
        self.ad = Ad.objects.create(
            property=self.property, platform="AirBnb", platform_fee=20.00
        )
        self.factory = APIRequestFactory()

    def test_list_ads(self):
        request = self.factory.get('/ads/')
        view = AdViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_ad(self):
        data = {
            "property": self.property.id,
            "platform": "Booking",
            "platform_fee": 15.00,
        }
        request = self.factory.post('/ads/', data)
        force_authenticate(request, user=self.user)
        view = AdViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Ad.objects.count(), 2)
        self.assertEqual(Ad.objects.last().platform, "Booking")

    def test_update_ad(self):
        data = {
            "platform": "Booking",
            "platform_fee": 15.00,
        }
        request = self.factory.patch('/ads/{}/'.format(self.ad.id), data)
        force_authenticate(request, user=self.user)
        view = AdViewSet.as_view({'patch': 'update'})
        response = view(request, pk=self.ad.id)
        self.assertEqual(response.status_code, 200)
        self.ad.refresh_from_db()
        self.assertEqual(self.ad.platform, "Booking")
    
    def test_delete_ad(self):
        request = self.factory.delete('/ads/{}/'.format(self.ad.id))
        force_authenticate(request, user=self.user)
        view = AdViewSet.as_view({'delete': 'destroy'})
        response = view(request, pk=self.ad.id)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Ad.objects.count(), 0)