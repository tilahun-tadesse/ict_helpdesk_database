# Generated by Django 4.2.3 on 2023-07-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_ask_help',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('expert_id', models.CharField(max_length=50)),
                ('problem_catagory', models.CharField(max_length=50)),
                ('device_name', models.CharField(max_length=50)),
                ('problem_discription', models.CharField(max_length=500)),
                ('problem_priority', models.CharField(max_length=50)),
                ('campus', models.CharField(max_length=50)),
                ('building_area', models.CharField(max_length=50)),
                ('room', models.CharField(max_length=40)),
            ],
        ),
    ]
