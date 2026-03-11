from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from ..models import Tratamientos
from ..serializers import TratamientosSerializer
from ..auth.permissions import IsAdminOrReadOnly

class TratamientosViewSet(viewsets.ModelViewSet):
    queryset = Tratamientos.objects.all().order_by("nombre")
    serializer_class = TratamientosSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["nombre","descripcion"]
    ordering_fields = ["nombre","precio"]