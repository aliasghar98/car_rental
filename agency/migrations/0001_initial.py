# Generated by Django 3.1.2 on 2020-12-25 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKING',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('pickup_location', models.TextField(blank=True, default='')),
                ('is_driver_needed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DRIVER',
            fields=[
                ('CNIC', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('hourly_rate', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FARE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_type', models.CharField(choices=[('ECO', 'ECONOMY'), ('BIZ', 'BUSINESS'), ('LUX', 'LUXURY')], max_length=100)),
                ('car_fare', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RENTAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_delivery', models.DateTimeField()),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='agency.booking')),
            ],
        ),
        migrations.CreateModel(
            name='CAR_MODEL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.PositiveIntegerField()),
                ('body_type', models.CharField(choices=[('SDN', 'SEDAN'), ('CPE', 'COUPE'), ('STW', 'STATION WAGON'), ('HTB', 'HATCHBACK'), ('CNV', 'CONVERTABLE')], max_length=100)),
                ('engine_capacity', models.PositiveIntegerField()),
                ('seats', models.PositiveIntegerField()),
                ('transmission', models.CharField(choices=[('MAN', 'MANUAL'), ('AUT', 'AUTOMATIC')], max_length=100)),
            ],
            options={
                'unique_together': {('make', 'model')},
            },
        ),
        migrations.CreateModel(
            name='CAR',
            fields=[
                ('reg_no', models.CharField(default='', max_length=25, primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=100)),
                ('fuel', models.CharField(choices=[('PET', 'PETROL'), ('DSL', 'DIESEL')], max_length=100)),
                ('image', models.ImageField(default='default_car.png', upload_to='car_pics')),
                ('accident_details', models.TextField(blank=True, default='')),
                ('available', models.BooleanField(default=True)),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agency.car_model')),
                ('fare', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agency.fare')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='allocated_car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agency.car'),
        ),
        migrations.AddField(
            model_name='booking',
            name='allocated_driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='agency.driver'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
