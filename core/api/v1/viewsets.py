from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from core.models import Perfil, Livro, Troca, Avaliacao
from .serializers import PerfilSerializer, LivroSerializer, TrocaSerializer, AvaliacaoSerializer

class SoftDeleteModelViewSet(viewsets.ModelViewSet):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PerfilViewSet(SoftDeleteModelViewSet):
    queryset = Perfil.objects.filter(is_deleted=False)
    serializer_class = PerfilSerializer

class LivroViewSet(SoftDeleteModelViewSet):
    queryset = Livro.objects.filter(is_deleted=False)
    serializer_class = LivroSerializer

class TrocaViewSet(SoftDeleteModelViewSet):
    queryset = Troca.objects.filter(is_deleted=False)
    serializer_class = TrocaSerializer

class AvaliacaoViewSet(SoftDeleteModelViewSet):
    queryset = Avaliacao.objects.filter(is_deleted=False)
    serializer_class = AvaliacaoSerializer