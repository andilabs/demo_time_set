from django.db import models


class DemoClass(models.Model):
    title = models.CharField(max_length=255)
    timestamp_from = models.DateTimeField()
    timestamp_to = models.DateTimeField()
