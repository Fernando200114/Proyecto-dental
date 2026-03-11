from ..models import Historial
from rest_framework import serializers


class HistorialSerializer(serializers.ModelSerializer):

    paciente_nombre = serializers.CharField(
        source="paciente.nombre",
        read_only=True
    )

    tratamiento_nombre = serializers.CharField(
        source="tratamiento.nombre",
        read_only=True
    )

    class Meta:
        model = Historial
        fields = "__all__"