from django.test import TestCase, Client
from django.urls import reverse

from apps.property.models import Property

class PropertyViewSetTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.property_data = {'name': 'Test Property', 'location': 'Test Location'}
        self.property = Property.objects.create(**self.property_data)
        self.url = reverse('property-list')
    
    def test_get_all_properties(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Test Property')
    
    def test_create_property(self):
        response = self.client.post(self.url, data=self.property_data)
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Property.objects.count(), 2)
        self.assertEqual(Property.objects.get(pk=response.data['id']).name, 'Test Property')
    
    def test_update_property(self):
        updated_data = {'name': 'Updated Property', 'location': 'Updated Location'}
        response = self.client.put(reverse('property-detail', kwargs={'pk': self.property.pk}), data=updated_data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Property.objects.get(pk=self.property.pk).name, 'Updated Property')
    
    def test_delete_property(self):
        response = self.client.delete(reverse('property-detail', kwargs={'pk': self.property.pk}))
        
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Property.objects.count(), 0)
    
    def test_create_property_with_invalid_data(self):
        invalid_property_data = {'name': '', 'location': 'Test Location'}
        response = self.client.post(self.url, data=invalid_property_data)

        self.assertEqual(response.status_code, 400)