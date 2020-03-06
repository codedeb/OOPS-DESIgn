from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    musician = models.Model.ForeignKey(Musician, on_delete = models.CASCADE, null = True)
    release_date = models.DateField(auto_add = True)