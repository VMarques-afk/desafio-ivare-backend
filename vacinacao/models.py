from django.db import models
from django.contrib.auth.models import AbstractUser


class Pet(models.Model):
    ESPECIE_CHOICES = [
        ('C', 'Cachorro'),
        ('G', 'Gato'),
        ('O', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=1, choices=ESPECIE_CHOICES)
    raca = models.CharField(max_length=50, blank=True)

    dono = models.ForeignKey(
        Usuario, related_name='pets', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.dono.username})"


class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} - {self.fabricante}"


class RegistroVacinacao(models.Model):
    pet = models.ForeignKey(
        Pet, related_name='vacinacoes', on_delete=models.CASCADE)
    vacina = models.ForeignKey(
        Vacina, related_name='aplicacoes', on_delete=models.PROTECT)
    data_aplicacao = models.DateField(auto_now_add=True)
    proxima_dose = models.DateField(null=True, blank=True)
    veterinario_responsavel = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.pet.nome} tomou {self.vacina.nome} em {self.data_aplicacao}"
