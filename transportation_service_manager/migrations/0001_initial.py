# Generated by Django 5.1.7 on 2025-04-06 10:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ocean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StatusTransportationService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('Pending', 'Waiting For Payment'), ('Paid', 'Payment Confirmed'), ('Ticket Issued', 'Ticket Issued'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Refunded', 'Refunded'), ('Checked In', 'Checked In'), ('Boarded', 'On Board'), ('Delayed', 'Delayed'), ('Completed', 'Completed'), ('Expired', 'Expired'), ('No Show', 'No Show'), ('Refund Requested', 'Refund Requested'), ('Refund Approved', 'Refund Approved'), ('Refund Denied', 'Refund Denied'), ('Refund Processed', 'Refund Processed'), ('Refund Completed', 'Refund Completed')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Cruise Ship', 'Cruise Ship'), ('Ocean Liner', 'Ocean Liner'), ('Ferry', 'Ferry')], max_length=100)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ports_city', to='transportation_service_manager.city')),
                ('ocean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ports_ocean', to='transportation_service_manager.ocean')),
            ],
        ),
        migrations.CreateModel(
            name='PortVisit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('current_port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portvisit_current', to='transportation_service_manager.port')),
                ('port_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portvisit_desitnation', to='transportation_service_manager.port')),
                ('current_vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portvisit_vehicle', to='transportation_service_manager.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='TransportationService',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('port_visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportation_service_port_visit', to='transportation_service_manager.portvisit')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportation_service_status', to='transportation_service_manager.statustransportationservice')),
            ],
        ),
    ]
