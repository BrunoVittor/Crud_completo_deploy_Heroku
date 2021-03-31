from django.urls import path, include
from .views import car_list, car_create, car_update

urlpatterns = [
    path('', car_list, name='car_list'),
    path('new', car_create, name='car_create'),
    path('update/<int:id>/', car_update, name='car_update')
]
