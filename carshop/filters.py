import django_filters
import carshop.models
from django.db.models import Q

class Car(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Цена от и до')
    available = django_filters.BooleanFilter(method='filter_available', label='С пробегом')
    term = django_filters.CharFilter(method='filter_term', label='')


    class Meta:
        model = carshop.models.Car
        fields = ['price_range', 'available', 'term']

    def filter_available(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(mileage__gt=0)
        return queryset.filter(mileage=0)

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(title__icontains=term) |Q(description__icontains=term)

        return queryset.filter(criteria).distinct()