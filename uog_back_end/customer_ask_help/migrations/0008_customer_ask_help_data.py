# Generated by Django 4.2.3 on 2023-09-10 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer_ask_help', '0007_rename_building_area_customer_ask_help_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_ask_help',
            name='data',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
