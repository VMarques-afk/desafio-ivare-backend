from rest_framework import serializers
from .models import Usuario, Pet, Vacina, RegistroVacinacao


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario

        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)
        return user


class PetSerializer(serializers.ModelSerializer):
    especie_extenso = serializers.CharField(
        source='get_especie_display', read_only=True)
    raca_nome = serializers.CharField(source='raca.nome', read_only=True)
    dono_nome = serializers.CharField(source='dono.username', read_only=True)

    class Meta:
        model = Pet
        fields = ('id', 'nome', 'especie', 'especie_extenso', 'raca',
                  'raca_nome', 'data_nascimento', 'dono', 'dono_nome')


class PetAdminSerializer(serializers.ModelSerializer):
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
