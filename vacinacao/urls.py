from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PetViewSet, VacinaViewSet, RegistroVacinacaoViewSet

# O Router cria as URLs automaticamente (/pets/, /pets/1/, etc)
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pets', PetViewSet)
router.register(r'vacinas', VacinaViewSet)
router.register(r'registros', RegistroVacinacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
