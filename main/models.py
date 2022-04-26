from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=36)
    age = models.IntegerField()

