"""
URL configuration for car_shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os.path import basename

from django.contrib import admin
from django.urls import path

from carshop.serializers import Storage
from carshop.views import FirstView, CarList, CarDelete, CarDetail, CarUpdate, CarCreate
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from carshop.views import OwnerAPI, StorageAPI, BuyerAPI, CarAPI, OrderAPI
from drf_spectacular.views import SpectacularAPIView,  SpectacularSwaggerView

router = DefaultRouter()

router.register('owners', OwnerAPI, basename='owners')
router.register('storages', StorageAPI, basename='storages')
router.register('buyers', BuyerAPI, basename='buyers')
router.register('cars', CarAPI, basename='cars')
router.register('orders', OrderAPI, basename='orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_view/', FirstView.as_view(), name='first_view'),
    # path('cars_list_template_view/', CarListTemplateView.as_view(), name='car_list_template_view'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('cars_list/', CarList.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car_detail'),
    path('cars/<int:pk>/update/', CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', CarDelete.as_view(), name='car_delete'),
    path('cars/add/', CarCreate.as_view(), name='car_create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + router.urls
