# Generated by Django 4.2.11 on 2024-04-15 17:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('area', models.CharField(blank=True, choices=[('kerala', 'kerala')], max_length=20, null=True)),
                ('borough', models.CharField(blank=True, max_length=50, null=True)),
                ('listing_type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Office', 'Office')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
