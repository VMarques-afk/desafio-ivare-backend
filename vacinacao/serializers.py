from rest_framework import serializers
from .models import Usuario, Pet, Vacina, RegistroVacinacao


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario

        fields = ['id', 'username', 'email', 'celular', 'password']

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = '__all__'


class RegistroVacinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroVacinacao
        fields = '__all__'
