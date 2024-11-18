from django.db import models
from uuid import uuid4

class Evento(models.Model):
    id_eventos = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    Ano_lancamento = models.IntegerField()
    DiaAdi = models.DateField(auto_now_add=True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=35)
    email = models.EmailField()
    Evento = models.ForeignKey(Evento, related_name='participantes', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
