# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pathlab',
            fields=[
                ('Path_Lab_Id', models.IntegerField(default=b'', primary_key=True, serialize=False)),
                ('Path_Lab_Password', models.CharField(default=b'', max_length=20)),
                ('Path_Lab_Name', models.CharField(default=b'', max_length=200)),
                ('Basic_Contact_number', models.CharField(default=b'', max_length=20)),
                ('Alternate_Contact_number', models.CharField(default=b'', max_length=20)),
                ('Home_Pick_up', models.BooleanField()),
                ('Account_Number', models.CharField(default=b'', max_length=200)),
                ('IFSC_Code', models.CharField(default=b'', max_length=200)),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Country', models.CharField(default=b'', max_length=200)),
            ],
            options={
                'db_table': 'pathlab',
            },
        ),
        migrations.CreateModel(
            name='pathlabinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=30)),
                ('Pincode', models.CharField(max_length=30)),
                ('Nearby_Pincode', models.CharField(max_length=30)),
                ('Basic_Contact_number', models.CharField(default=b'', max_length=20)),
                ('Alternate_Contact_number', models.CharField(default=b'', max_length=20)),
                ('Address_No1_Plot_Number', models.CharField(max_length=30)),
                ('Address_No2_Sub_Locality', models.CharField(max_length=100)),
                ('Address_No3_Area', models.CharField(max_length=100)),
                ('Is_Package', models.BooleanField()),
                ('Package_Name', models.CharField(max_length=100)),
                ('Test_Day', models.CharField(default=b'', max_length=300)),
                ('Test_Name', models.CharField(max_length=30)),
                ('Test_Start_at', models.DateTimeField()),
                ('Test_End_at', models.DateTimeField()),
                ('Price', models.CharField(max_length=255)),
                ('Details', models.TextField()),
                ('Path_Lab_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.pathlab')),
            ],
            options={
                'db_table': 'pathlabinfo',
            },
        ),
    ]