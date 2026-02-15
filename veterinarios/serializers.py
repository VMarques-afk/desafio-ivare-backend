from rest_framework import serializers
from .models import Veterinario

class VeterinarioSerializer(serializers.ModelSerializer):
    username_login = serializers.CharField(source='user.name', read_only=True)

class Meta:
    model = Veterinario
    fields = ['id', 'user', 'username_login','nome', 'sobrenome', 'crmv', 'telefone']