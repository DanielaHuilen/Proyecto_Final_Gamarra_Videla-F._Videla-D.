from django.db import models

# Create your models here.

class Profesores (models.Model):
    nombre= models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    antiguedad=models.IntegerField()
    asignatura=models.CharField(max_length=20)
    
    def __str__ (self):
        return f"Docente: {self.apellido} {self.nombre}, docente de {self.asignatura} "