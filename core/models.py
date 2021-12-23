from django.db import models

class Thing(models.Model):
    color = models.CharField(max_length=10)

    __str__ = __repr__ = lambda self: self.color