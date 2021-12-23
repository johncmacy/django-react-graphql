from django.db import models
from django.conf import settings

class Shape(models.Model):
    name = models.CharField(max_length=10)

    __str__ = __repr__ = lambda self: self.name

class Color(models.Model):
    name = models.CharField(max_length=10)

    __str__ = __repr__ = lambda self: self.name

class Thing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='things')
    name = models.CharField(max_length=20)

    __str__ = __repr__ = lambda self: self.name

class Widget(models.Model):
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, related_name='widgets')
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, related_name='things')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='things')
    number = models.IntegerField(default=1)

    __str__ = __repr__ = lambda self: f'{self.thing} has {self.number} {self.color} {self.shape}(s)'
