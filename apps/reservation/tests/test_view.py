from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory
from apps.reservation.models import Reservation
from apps.ad.models import Ad
from apps.reservation.views import ReservationViewSet

class ReservationViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
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
        self.view = ReservationViewSet.as_view({'get': 'list'})
    
    def test_list_view(self):
        request = self.factory.get('/reservations/')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['code'], 'TEST123')
        self.assertEqual(response.data[0]['ad'], self.ad.pk)
        self.assertEqual(response.data[0]['check_in'], '2022-01-01')
        self.assertEqual(response.data[0]['check_out'], '2022-01-07')
        self.assertEqual(response.data[0]['total_price'], '200.00')
        self.assertEqual(response.data[0]['comment'], 'Test reservation')
        self.assertEqual(response.data[0]['num_guests'], 2)

    def test_create_view(self):
        data = {
            'code': 'TEST124',
            'ad': self.ad.pk,
            'check_in': '2022-02-01',
            'check_out': '2022-02-07',
            'total_price': '250.00',
            'comment': 'Test reservation 2',
            'num_guests': 3
        }
        request = self.factory.post('/reservations/', data)
        response = self.view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Reservation.objects.count(), 2)
        new_reservation = Reservation.objects.get(code='TEST124')
        self.assertEqual(new_reservation.ad.pk, self.ad.pk)
        self.assertEqual(str(new_reservation.check_in), '2022-02-01')
        self.assertEqual(str(new_reservation.check_out), '2022-02-07')
        self.assertEqual(str(new_reservation.total_price), '250.00')
       
