from rest_framework import serializers
from app1.models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['id', 'titulo', 'descripcion', 'fecha', 'imagen', 'enlace']
        read_only_fields = ['id']
