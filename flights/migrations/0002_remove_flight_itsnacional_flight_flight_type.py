# Generated by Django 5.1.6 on 2025-02-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='itsNacional',
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_type',
            field=models.CharField(default='Nacional', max_length=100),
        ),
    ]
