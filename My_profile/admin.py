# -*- coding: utf-8 -*-


# Register your models here.

from django.contrib import admin
from .import models


admin.site.register(models.Information)
admin.site.register(models.Address)
admin.site.register(models.Contact_Info)



