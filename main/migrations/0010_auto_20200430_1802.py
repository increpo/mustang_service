# Generated by Django 3.0.5 on 2020-04-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_car_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='spare',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
