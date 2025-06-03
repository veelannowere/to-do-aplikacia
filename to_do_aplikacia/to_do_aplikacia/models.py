from django.db import models

class Task(models.Model):
  nazov = models.CharField(max_length=255)
  popis = models.TextField(max_length=255)
  datum = models.DateField(max_length=255)
  priorita = models.CharField(max_length=50)
  pouzivatel = models.ForeignKey(max_length=255)  