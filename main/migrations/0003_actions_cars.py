# Generated by Django 3.0.5 on 2020-04-28 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200428_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='cars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Cars'),
        ),
    ]
