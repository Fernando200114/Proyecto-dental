from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Pacientes
from ..serializers import PacientesSerializer
from ..auth.permissions import IsAdminOrReadOnly


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all().order_by("-id")
    serializer_class = PacientesSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields= ["nombre","apellido","cedula","telefono"]
    ordering_fields= ["id","nombre","apellido","fecha_registro"]
    