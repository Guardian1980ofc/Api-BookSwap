# É o responsável por gerar automaticamente as URLs da API baseado nos ViewSets registrados.

from rest_framework.routers import DefaultRouter
from .viewsets import PerfilViewSet, LivroViewSet, TrocaViewSet, AvaliacaoViewSet

router = DefaultRouter() # instancia o roteador padrão do Django REST Framework
router.register(r'perfis', PerfilViewSet) # registra o ViewSet de Perfis
router.register(r'livros', LivroViewSet) # registra o ViewSet de Livros
router.register(r'trocas', TrocaViewSet) # registra o ViewSet de Trocas
router.register(r'avaliacoes', AvaliacaoViewSet) # registra o ViewSet de Avaliações

urlpatterns = router.urls # expõe as URLs geradas pelo roteador para serem usadas na configuração de URLs do Django
