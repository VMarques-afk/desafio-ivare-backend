from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Raca(models.Model):
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('outro', 'Outro'),
    ]

    def __str__(self):
        return f"{self.nome}({self.get_especie_display()})"

    nome = models.CharField(max_length=100, verbose_name="Nome da raça")
    especie = models.CharField(
        max_length=20, choices=ESPECIE_CHOICES, verbose_name="Espécie")

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"


class Pet(models.Model):
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('outro', 'Outro'),
    ]
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIE_CHOICES)

    raca = models.ForeignKey(
        Raca, on_delete=models.SET_NULL, null=True, blank=True, related_name='pets')

    data_nascimento = models.DateField(null=True, blank=True)

    dono = models.ForeignKey(
        'Usuario', related_name='pets', on_delete=models.CASCADE)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.dono.username})"


class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} - {self.fabricante}"

    class Meta:
        verbose_name = "Vacina"
        verbose_name_plural = "Vacinas"


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

    class Meta:
        verbose_name_plural = "Registro de vacinações"
