# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('detailId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('remains', models.IntegerField()),
                ('memo', models.CharField(max_length=200)),
                ('c_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailId', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('memo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detailId', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('memo', models.CharField(max_length=200)),
            ],
        ),
    ]
