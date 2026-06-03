from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' # Incluye id, nombre, descripcion, precio, imagen y creado_en