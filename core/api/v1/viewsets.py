#É o responsável por definir o que a API pode fazer com cada model

from rest_framework import viewsets
from core.models import Perfil, Livro, Troca, Avaliacao
from .serializers import PerfilSerializer, LivroSerializer, TrocaSerializer, AvaliacaoSerializer

class PerfilViewSet(viewsets.ModelViewSet): # classe que define as operações CRUD para o modelo Perfil
    queryset = Perfil.objects.filter(is_deleted=False) # define o conjunto de dados que será manipulado pela API, nesse caso, apenas os perfis que não foram marcados como deletados
    serializer_class = PerfilSerializer # define o serializer que será usado para converter os dados do modelo Perfil para JSON e vice-versa

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.filter(is_deleted=False)
    serializer_class = LivroSerializer

class TrocaViewSet(viewsets.ModelViewSet):
    queryset = Troca.objects.filter(is_deleted=False)
    serializer_class = TrocaSerializer

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.filter(is_deleted=False)
    serializer_class = AvaliacaoSerializer

