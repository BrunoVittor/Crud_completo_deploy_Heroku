from .models import Cars
from django.forms import ModelForm


class Car_form(ModelForm):
    class Meta:
        model = Cars
        fields = ['car_name', 'car_model', 'car_color', 'car_year', 'car_value', 'car_description', 'car_image',]
