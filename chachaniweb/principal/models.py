from __future__ import unicode_literals

from django.db import models, Field

# Create your models here.

class mensaje(models.Model):
    apellidos = models.CharField(max_length = 50)
    nombres = models.CharField(max_length = 50)
    num_proveedor = models.IngerField(Field.blank = True)
    correo = models.CharField(max_length = 80)
