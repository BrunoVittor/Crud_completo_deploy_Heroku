# Generated by Django 2.2.19 on 2021-04-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20210331_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='cars_photos'),
        ),
    ]
