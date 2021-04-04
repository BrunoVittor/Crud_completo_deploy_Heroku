from django.urls import path, include
from .views import car_list, car_create, car_update, car_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', car_list, name='car_list'),
                  path('new', car_create, name='car_create'),
                  path('update/<int:id>/', car_update, name='car_update'),
                  path('delete/<int:id>/', car_delete, name='car_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
