# Generated by Django 3.0.5 on 2020-04-28 11:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('car_model', models.CharField(help_text="Enter car's model", max_length=50)),
                ('year_of_issue', models.DateField()),
                ('body_serial_number', models.CharField(max_length=20)),
                ('engine_serial_number', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text="Enter instrument's name", max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter service type name', max_length=50)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spares',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter spares name', max_length=50)),
                ('car_model', models.CharField(help_text="Enter car's model for spare", max_length=50)),
                ('release_date', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('operation_start_date', models.DateTimeField()),
                ('operation_finish_date', models.DateTimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('instrument_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Instruments')),
            ],
        ),
    ]
