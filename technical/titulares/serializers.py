from rest_framework import serializers

from technical.titulares.models import Juridica, Fisica


class FisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fisica
        fields = ['id', 'cuit', 'name', 'lastname', 'dni']


class JuridicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juridica
        fields = ['id', 'cuit', 'razonSoc', 'year']
