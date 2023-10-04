# countries/models.py

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    languages = models.ManyToManyField('Language')

class Language(models.Model):
    name = models.CharField(max_length=100)
