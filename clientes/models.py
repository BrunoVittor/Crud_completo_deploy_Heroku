from django.db import models

class Cars(models.Model):
    car_name = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=50)
    car_year = models.IntegerField()
    car_value = models.DecimalField(max_digits=10, decimal_places=2)
    car_description = models.TextField()


    def __str__(self):
        return self.car_name