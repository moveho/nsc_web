from django.db import models


class Kospi(models.Model):
    date = models.DateField(null=False, unique=True)
    close = models.FloatField(null=True)
    open = models.FloatField(null=True)
