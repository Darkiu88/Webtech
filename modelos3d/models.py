from django.db import models

# Create your models here.
class Modelo3D(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='modelos3d/')

    def __str__(self):
        return self.nombre