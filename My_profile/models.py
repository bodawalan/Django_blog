# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Information(models.Model):
    F_name = models.CharField(max_length=255)
    Age =models.IntegerField()
    GENDER_CHOICES=(
        ("M",'MALE'),
        ("F","FEMALE")
    )
    Gender  = models.CharField(max_length=1,choices=GENDER_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.F_name

class Address(models.Model):
    s_address = models.TextField(max_length=255)
    Zipcode =models.IntegerField()
    city=models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.Zipcode

class Contact_Info(models.Model):
    cell_number=models.IntegerField()
    Email=models.EmailField(max_length=50)
    Git_hub = models.URLField(max_length=200)

    def __str__(self):
        return self.Email


