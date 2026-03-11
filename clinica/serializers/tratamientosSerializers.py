from rest_framework import serializers
from ..models import Tratamientos

# SERIALIZER TRATAMIENTOS
class TratamientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamientos
        fields = "__all__"
