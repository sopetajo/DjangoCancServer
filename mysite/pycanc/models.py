# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Probe(models.Model):
    hostName = models.CharField(max_length=100)
    hostAdress = models.CharField(max_length=20)
    
class Command(models.Model):
    content = models.CharField(max_length=200)
    result = models.CharField(max_length=300)
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE)
