# Generated by Django 3.1.2 on 2020-12-23 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_booking_selected_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='selected_car',
            new_name='allocated_car',
        ),
        migrations.AddField(
            model_name='booking',
            name='allocated_driver',
            field=models.CharField(default='None', max_length=25),
            preserve_default=False,
        ),
    ]
