from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.TextField()
