# Generated by Django 5.0 on 2024-05-11 04:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_name', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('total_spaces', models.IntegerField()),
                ('free_spaces', models.IntegerField()),
                ('occupied_spaces', models.IntegerField()),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_space_status', models.CharField(max_length=50)),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parking_spaces', to='parking.parking')),
            ],
        ),
    ]