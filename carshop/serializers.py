from rest_framework import serializers
from carshop import models


class Owner(serializers.ModelSerializer):

    class Meta:
        model = models.Owner
        fields = '__all__'


class Storage(serializers.ModelSerializer):

    class Meta:
        model = models.Storage
        fields = '__all__'


class Buyer(serializers.ModelSerializer):

    class Meta:
        model = models.Buyer
        fields = '__all__'

class Car(serializers.ModelSerializer):
    owner = Owner(read_only=True)
    storage= Storage(read_only=True)
    owner_id = serializers.IntegerField(required=False, allow_null=True)
    storage_id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = models.Car
        fields = '__all__'

class Order(serializers.ModelSerializer):
    buyer = Buyer(read_only=True)
    car = Car(read_only=True)
    buyer_id = serializers.IntegerField(required=False, allow_null=True)
    car_id = serializers.IntegerField(required=False, allow_null=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = '__all__'

    def get_price(self, obj):
        return obj.id_car.price