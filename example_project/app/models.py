from __future__ import unicode_literals

from django.db import models

# Create your models here.

##from django.db import models

class ExampleDotCom(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title
