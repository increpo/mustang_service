# Generated by Django 3.0.5 on 2020-04-28 17:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20200428_1730'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actions',
            new_name='Action',
        ),
        migrations.RenameModel(
            old_name='Instruments',
            new_name='Instrument',
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
        migrations.RenameModel(
            old_name='Spares',
            new_name='Spare',
        ),
    ]
