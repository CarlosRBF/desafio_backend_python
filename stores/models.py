from django.db import models


class Stores(models.Model):
    store_name = models.CharField(max_length=155)
    store_owner = models.CharField(max_length=155)
    balance = models.FloatField(default=0)
