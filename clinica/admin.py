

# Register your models here.
from django.contrib import admin
from .models import Pacientes,Citas,Tratamientos,Historial


@admin.register(Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "cedula", "telefono", "email")
    search_fields = ("nombre","apellido","cedula")
    
@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    list_display = ("paciente","hora","fecha","estado")
    list_filter = ("estado","fecha")
    
@admin.register(Tratamientos)
class TratamientosAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio")
    
@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ("paciente","tratamiento","fecha")
    list_filter = ("fecha",)