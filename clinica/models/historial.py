from django.db import models
from .pacientes import Pacientes
from .tratamientos import Tratamientos

class Historial(models.Model):
    paciente = models.ForeignKey(Pacientes,on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamientos, on_delete=models.CASCADE)
    fecha = models.DateField(auto_created=True)
    notas = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.paciente}-{self.tratamiento}"
    
    
    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"
        ordering = ["-fecha"]

