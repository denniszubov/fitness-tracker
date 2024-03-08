# Generated by Django 5.0.3 on 2024-03-08 01:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('distance_km', models.DecimalField(decimal_places=3, max_digits=5)),
                ('duration', models.DurationField()),
                ('average_pace', models.DurationField()),
                ('average_heart_rate', models.IntegerField(blank=True, null=True)),
                ('elevation_gain', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('weather_conditions', models.CharField(blank=True, max_length=50, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='runs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
