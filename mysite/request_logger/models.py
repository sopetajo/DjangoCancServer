# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
#
@python_2_unicode_compatible
class Request_log(models.Model):
    log_content = models.CharField(max_length = 200)
    log_date = models.DateTimeField('date logged')

    def __str__(self):
        return self.log_content[0:10]

# Create your models here.
