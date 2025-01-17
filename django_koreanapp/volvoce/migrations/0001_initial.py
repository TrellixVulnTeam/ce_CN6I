# Generated by Django 2.1.7 on 2019-02-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerEmail', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=100)),
                ('companyAddress', models.CharField(max_length=300)),
                ('no_working_days', models.IntegerField(default=22)),
            ],
        ),
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('JID', models.IntegerField()),
                ('payout', models.FloatField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=200)),
                ('completed', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('machine_hour', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(max_length=100)),
                ('model_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OneTimePassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField()),
                ('ownerEmail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OperatorJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JID', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('vehicle_serial_no', models.CharField(max_length=100)),
                ('vehicle_model_no', models.CharField(max_length=100)),
                ('pay_received', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OperatorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownerEmail', models.CharField(max_length=100)),
                ('operatorEmail', models.CharField(max_length=100)),
                ('is_delete', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OperatorVehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opEmail', models.CharField(max_length=100)),
                ('vtype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('serial_no', models.CharField(max_length=100)),
                ('model_no', models.CharField(max_length=100)),
                ('JID', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('report_type', models.CharField(default='Job Report', max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='jobReport/')),
                ('desc', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
                ('faults', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(null=True)),
                ('role', models.IntegerField()),
                ('profile_image_url', models.CharField(default='', max_length=200)),
                ('access_token', models.CharField(max_length=200)),
                ('companyName', models.CharField(max_length=100, null=True)),
                ('phoneNumber', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vtype', models.CharField(max_length=100)),
                ('ImgUrl', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('serial_no', models.CharField(max_length=100)),
                ('model_no', models.CharField(max_length=100)),
                ('purchase_date', models.DateField()),
                ('desc', models.CharField(max_length=1000)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('is_delete', models.IntegerField()),
            ],
        ),
    ]
