from django.db import models
from .pacientes import Pacientes



class Citas(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "Pendiente", "Pendiente"
        RESERVADO = "Reservado", "Reservado"
        CANCELADO = "Cancelado", "Cancelado"
        FINALIZADO = "Finalizado", "Finalizado"
    
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length = 120)
    estado = models.CharField(max_length=20,choices = Estado.choices,default=Estado.PENDIENTE)
    
    def __str__(self):
        return f"Cita de {self.paciente} - {self.fecha}"
    
    class Meta:
        unique_together = ["fecha","hora"] 




