import factory
from factory.django import ImageField
from faker import Faker

from carshop import models

fake = Faker()

class OwnerFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('first_name')
    surname = factory.Faker('user_name')
    birthday = factory.Faker('date')


    class Meta:
        model = models.Owner

class StorageFactory(factory.django.DjangoModelFactory):
    street = factory.Faker('text')
    number_of_street = factory.LazyFunction(lambda: fake.random_int(min=1, max=100))


    class Meta:
        model = models.Storage




class CarFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    image = ImageField()
    price = factory.LazyFunction(lambda: fake.random_int(min=100, max=100000000))
    description = factory.Faker('text')
    mileage = factory.LazyFunction(lambda: fake.random_int(min=100, max=1000000))
    id_owner = factory.SubFactory(OwnerFactory)
    id_storage = factory.SubFactory(StorageFactory)


    class Meta:
        model = models.Car