from rest_framework import viewsets
from app1.models import Proyecto
from .serializers import ProyectoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all().order_by('-fecha')
    serializer_class = ProyectoSerializer

