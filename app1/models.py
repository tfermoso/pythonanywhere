from django.db import models

# Create your models here.


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='proyectos/')  # sube a /media/proyectos/
    enlace = models.URLField(verbose_name='Repositorio GitHub')
    url = models.URLField(verbose_name='URL del proyecto del alumno', blank=True, null=True)

    def __str__(self):
        return self.titulo
