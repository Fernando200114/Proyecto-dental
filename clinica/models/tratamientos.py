from django.db import models 


class Tratamientos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    def __str__(self):
        return self.nombre
  
        
    
    
