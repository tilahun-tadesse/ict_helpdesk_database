# Generated by Django 4.2.3 on 2023-08-01 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_ask_help', '0006_customer_ask_help_problem_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer_ask_help',
            old_name='building_area',
            new_name='building',
        ),
    ]