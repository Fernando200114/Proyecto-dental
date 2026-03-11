from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models import Citas
from ..serializers import CitasSerializer
from ..auth.permissions import IsAdminOrReadOnly
from ..services.whatsapp_service import enviar_whatsapp


class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.select_related("paciente").all().order_by("-fecha")
    serializer_class = CitasSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["estado", "fecha"]
    search_fields = ["paciente__nombre", "motivo"]
    ordering_fields = ["fecha", "hora", "estado"]


    def perform_create(self, serializer):
        cita = serializer.save()
        paciente = cita.paciente
        mensaje = f"""
        
Hola {paciente.nombre} 👋
Le recordamos su cita odontológica


📅 Fecha: {cita.fecha}
⏰ Hora: {cita.hora}
Clínica Dental
"""

        enviar_whatsapp(paciente.telefono, mensaje)