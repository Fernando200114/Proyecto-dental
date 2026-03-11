from django.db import models

class Pacientes(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120) 
    cedula = models.CharField(max_length=10,unique=True)
    telefono = models.CharField(max_length=13)
    email = models.EmailField() 
    direccion = models.CharField(max_length=120)
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["nombre"]