#from __future__ import unicode_literals

from django.db import models

# Create your models here.

class mensaje(models.Model):
    apellidos = models.CharField(max_length = 50)
    nombres = models.CharField(max_length = 50)
    num_proveedor = models.IntegerField(null = True)
    correo = models.EmailField()
    dia = models.DateTimeField()
    departamento = models.CharField(max_length = 30)
    provincia = models.CharField(max_length = 30)
    mensaje = models.TextField()
    contestado = models.BooleanField(default = False)

    def __str__(self):
        return self.nombres + " " +self.apellidos
