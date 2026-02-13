from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Pet, Vacina, RegistroVacinacao
from .serializers import (
    UsuarioSerializer,
    PetSerializer,
    VacinaSerializer,
    RegistroVacinacaoSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return Pet.objects.all()
        return Pet.objects.filter(dono=user)
    


class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer


class RegistroVacinacaoViewSet(viewsets.ModelViewSet):
    queryset = RegistroVacinacao.objects.all()
    serializer_class = RegistroVacinacaoSerializer
    permission_classes =  [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return RegistroVacinacao.objects.all()
        return RegistroVacinacao.objects.filter(pet_dono=user)