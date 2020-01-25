from django.db import models


class Link(models.Model):
    title = models.CharField(max_length=255)
    body  = models.CharField(max_length=255)
    rate  = models.PositiveIntegerField()

    def __str__(self):
        return self.title