#É o responsável por converter os dados do banco (objetos Python) em JSON para a API

from rest_framework import serializers
from core.models import Perfil, Livro, Troca, Avaliacao

class PerfilSerializer(serializers.ModelSerializer): # classe que define como o modelo Perfil será convertido para JSON e vice-versa
    class Meta:
        model = Perfil # modelo que será serializado
        fields = ['id', 'usuario', 'nome', 'cidade', 'created_at', 'updated_at'] #campos que serão expostos na API
        read_only_fields = ['created_at', 'updated_at'] # campos que o usuário não pode enviar, só receber

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'perfil', 'titulo', 'autor', 'isbn', 'estado', 'disponivel', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class TrocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Troca
        fields = ['id', 'solicitante', 'livro_ofertado', 'livro_desejado', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'troca', 'avaliador', 'nota', 'comentario', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

