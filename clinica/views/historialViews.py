from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Historial
from ..serializers import HistorialSerializer
from ..auth.permissions import IsAdminOrReadOnly

class HistorialViewSet(viewsets.ModelViewSet):
    queryset = Historial.objects.select_related("paciente","tratamiento" ).all().order_by("-fecha")
    serializer_class = HistorialSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["paciente","tratamiento","fecha"]
    search_fields = ["paciente__nombre","tratamiento__nombre"]
    ordering_fields = ["fecha"]