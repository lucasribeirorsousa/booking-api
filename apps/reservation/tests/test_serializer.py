from django.test import TestCase
from apps.reservation.models import Reservation
from apps.ad.models import Ad
from apps.reservation.serializers import ReservationSerializer

class ReservationSerializerTestCase(TestCase):
    def setUp(self):
        self.ad = Ad.objects.create(name='Test Ad')
        self.reservation = Reservation.objects.create(
            code='TEST123',
            ad=self.ad,
            check_in='2022-01-01',
            check_out='2022-01-07',
            total_price='200.00',
            comment='Test reservation',
            num_guests=2
        )
        self.serializer = ReservationSerializer(instance=self.reservation)
        self.data = self.serializer.data
    
    def test_contains_expected_fields(self):
        # Ensure the serializer contains all fields from the model
        fields = ['code', 'ad', 'check_in', 'check_out', 'total_price', 'comment', 'num_guests', 'created_at', 'updated_at']
        for field in fields:
            self.assertIn(field, self.data)
    
    def test_code_field_content(self):
        # Ensure the `code` field has the correct value
        self.assertEqual(self.data['code'], 'TEST123')
    
    def test_ad_field_content(self):
        # Ensure the `ad` field has the correct value
        self.assertEqual(self.data['ad'], self.ad.pk)
    
    def test_check_in_field_content(self):
        # Ensure the `check_in` field has the correct value
        self.assertEqual(self.data['check_in'], '2022-01-01')
    
    def test_check_out_field_content(self):
        # Ensure the `check_out` field has the correct value
        self.assertEqual(self.data['check_out'], '2022-01-07')

    def test_total_price_field_content(self):
        # Ensure the `total_price` field has the correct value
        self.assertEqual(self.data['total_price'], '200.00')

    def test_comment_field_content(self):
        # Ensure the `comment` field has the correct value
        self.assertEqual(self.data['comment'], 'Test reservation')

    def test_num_guests_field_content(self):
        # Ensure the `num_guests` field has the correct value
        self.assertEqual(self.data['num_guests'], 2)