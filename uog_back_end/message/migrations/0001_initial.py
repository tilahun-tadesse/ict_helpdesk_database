# Generated by Django 4.2.3 on 2023-07-29 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_number', models.CharField(max_length=50)),
                ('to_number', models.CharField(max_length=50)),
                ('message_text', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('message_seen', models.CharField(max_length=50)),
                ('expert_in', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user_information')),
            ],
        ),
    ]