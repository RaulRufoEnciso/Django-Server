from rest_framework import serializers
from cataleg.models import Producto

class CarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'