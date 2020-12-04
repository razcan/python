from django.db import models

class Info(models.Model):
    distance = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
