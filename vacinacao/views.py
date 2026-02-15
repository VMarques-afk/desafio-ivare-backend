from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Pet, Vacina, RegistroVacinacao
from .serializers import (
    UsuarioSerializer,
    PetSerializer,
    VacinaSerializer,
    RegistroVacinacaoSerializer,
    PetAdminSerializer,
)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return PetAdminSerializer
        return PetSerializer

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['especie', 'raca']
    search_fields = ['nome']
    ordering_fields = ['nome', 'id']

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return Pet.objects.all()
        return Pet.objects.filter(dono=user)

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            serializer.save()
        else:
            serializer.save(dono=self.request.user)


class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer


class RegistroVacinacaoViewSet(viewsets.ModelViewSet):
    queryset = RegistroVacinacao.objects.all()
    serializer_class = RegistroVacinacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return RegistroVacinacao.objects.all()
        return RegistroVacinacao.objects.filter(pet__dono=user)
