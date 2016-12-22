# -*- coding: utf-8 -*-
from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)


class Category(models.Model):
    c_id = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=20)


class Details(models.Model):
    detailId = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.FloatField()
    remains = models.IntegerField()
    memo = models.CharField(max_length=200)
    c_id = models.IntegerField()


class Income(models.Model):
    detailId = models.CharField(max_length=50)
    number = models.IntegerField()
    date = models.DateField()
    memo = models.CharField(max_length=200)


class Outcome(models.Model):
    detailId = models.CharField(max_length=50)
    number = models.IntegerField()
    date = models.DateField()
    memo = models.CharField(max_length=200)

# Create your models here.

