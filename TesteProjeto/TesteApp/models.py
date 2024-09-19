from django.db import models

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    telefone = models.IntegerField()