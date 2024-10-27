from django.test import TestCase
from django.urls import reverse
from carshop import factories, models

# Create your tests here.
class CarShopTestCase(TestCase):

    def setUp(self):
        self.owner = factories.OwnerFactory()
        self.storage = factories.StorageFactory()
        self.car = factories.CarFactory(id_owner=self.owner, id_storage=self.storage)

    def test_get_cars_list(self):
        url = reverse('car_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['cars'].count(), models.Car.objects.count())


    def test_get_car_detail(self):
        url = reverse('car_detail', kwargs={'pk': self.car.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_update_car(self):
        old_title = self.car.title
        response = self.client.post(reverse('car_update', kwargs={'pk': self.car.pk}), {'title': 'new_title'})
        self.car.refresh_from_db()
        self.assertEqual(old_title, self.car.title)
        self.assertEqual(response.status_code, 200)


    def test_delete_car(self):
        old_count = models.Car.objects.count()
        response = self.client.delete(reverse('car_delete', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(old_count-1, models.Car.objects.count())

    def test_create_car(self):
        start = models.Car.objects.count()
        url = reverse('car_create')
        response = self.client.post(url, {
            'title': 'Honda Civic',
            'image': 'images/4.jpg',
            'price': 5,
            'description': 'Новая Машина',
            'mileage': 10000,
            'id_owner': self.owner.pk,
            'id_storage': self.storage.pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(start+1, models.Car.objects.count())




