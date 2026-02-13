from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PetViewSet, VacinaViewSet, RegistroVacinacaoViewSet

#router associa o Url a um conjunto de visões gerando rotas padrão da API GPPD
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pets', PetViewSet)
router.register(r'vacinas', VacinaViewSet)
router.register(r'registros', RegistroVacinacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
