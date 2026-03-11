from django.urls import path
from rest_framework.routers import DefaultRouter

# Importa los ViewSets desde los módulos específicos dentro de views
from .views.pacientesViews import PacienteViewSet
from .views.citasViews import CitasViewSet
from .views.tratamientosView import TratamientosViewSet
from .views.historialViews import HistorialViewSet

from .views.webhook_whatsapp import whatsapp_webhook

router = DefaultRouter()
router.register(r"paciente", PacienteViewSet, basename="paciente")
router.register(r"citas", CitasViewSet, basename="citas")
router.register(r"tratamientos", TratamientosViewSet, basename="tratamientos")
router.register(r"historial", HistorialViewSet, basename="historial")

# No es o no tiene un crud por eso se define de esta manera 
urlpatterns = [
    path("webhook-whatsapp/", whatsapp_webhook, name="webhook-whatsapp"),
]

urlpatterns += router.urls