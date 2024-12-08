from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from carshop.models import Car, Buyer, Owner, Storage, Order, HistoryOrder
from django_filters.views import FilterView
from carshop import filters
from rest_framework import viewsets
from carshop import serializers
from carshop import models
# Create your views here.




class OwnerAPI(viewsets.ModelViewSet):
    queryset = models.Owner.objects.all()
    serializer_class = serializers.Owner

class StorageAPI(viewsets.ModelViewSet):
    queryset = models.Storage.objects.all()
    serializer_class = serializers.Storage

class BuyerAPI(viewsets.ModelViewSet):
    queryset = models.Buyer.objects.all()
    serializer_class = serializers.Buyer

class CarAPI(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    serializer_class = serializers.Car

class OrderAPI(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.Order

class FirstView(View):
    def get(self, request):
        return HttpResponse('Привет джанго!')

'''class CarListTemplateView(TemplateView):
    template_name = 'car_shelf/car_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context'''

class CarList(FilterView):
    model = Car
    template_name = 'car_shelf/car_list.html'
    context_object_name = 'cars'
    filterset_class = filters.Car

class CarDetail(DetailView):
    model = Car
    template_name = 'car_shelf/car_detail.html'
    context_object_name = 'car'

class CarUpdate(UpdateView):
    model = Car
    template_name = 'car_shelf/car_form.html'
    fields = ['title', 'price', 'mileage', 'description']

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

class CarDelete(DeleteView):
    model = Car
    template_name = 'car_shelf/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')


class CarCreate(CreateView):
    model = Car
    template_name = 'car_shelf/car_create.html'
    fields = ['title','image', 'price', 'mileage', 'description', 'id_owner', 'id_storage']

    def get_success_url(self):
        return reverse_lazy('car_list')