from rest_framework import viewsets
from .models import Veterinario
from .serializers import VeterinarioSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer