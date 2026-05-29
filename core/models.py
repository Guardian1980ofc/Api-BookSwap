from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False) # Soft delete flag

    class Meta:
        abstract = True # não cria tabela, só serve de base para outros models

    def delete(self, *args, **kwargs): # Sobrescreve o método delete para realizar soft delete
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs): # Método para deletar permanentemente o registro
        super().delete(*args, **kwargs)

class Perfil(BaseModel):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):  
        return self.nome

class Livro(BaseModel):
    ESTADO_CHOICES = [
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('antigo', 'Antigo'),
    ]
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='livros')
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='novo')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Troca(BaseModel):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aceita', 'Aceita'),
        ('recusada', 'Recusada'),
        ('concluida', 'Concluída'),
    ]
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='trocas_solicitadas')
    livro_ofertado = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='trocas_ofertadas')
    livro_desejado = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='trocas_desejadas')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Troca: {self.solicitante.nome} - {self.livro_ofertado.titulo} por {self.livro_desejado.titulo} ({self.status})"

class Avaliacao(BaseModel):
    troca = models.ForeignKey(Troca, on_delete=models.CASCADE, related_name='avaliacoes')
    avaliador = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='avaliacoes_feitas')
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Avaliação: {self.nota}/5 por {self.avaliador} na troca {self.troca.id}"

