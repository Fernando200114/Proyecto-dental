from ..models import Citas
from rest_framework import serializers

# SERIALIZER CITAS
class CitasSerializer(serializers.ModelSerializer):

    paciente_nombre = serializers.CharField(
        source="paciente.nombre",
        read_only=True
    )

    class Meta:
        model = Citas
        fields = "__all__"
        
    def validate(self,data):
        fecha= data['fecha']
        hora = data['hora']
        
        if Citas.objects.filter(fecha=fecha,hora=hora).exists():
            raise serializers.ValidationError(
                "Este horario ya no esta reservado"
            )
        return data