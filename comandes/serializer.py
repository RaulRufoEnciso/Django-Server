from rest_framework import serializers
from .models import Comanda

class comandasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = '__all__'