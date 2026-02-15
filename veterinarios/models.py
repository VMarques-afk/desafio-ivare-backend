from django.db import models
from django.conf import settings


class Veterinario(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='Perfil_veterinario',
        null=True,
        blank=True
    )
    nome = models.CharField(max_length=150, verbose_name="Nome", blank=True)
    sobrenome = models.CharField(
        max_length=150, verbose_name="Sobrenome", blank=True)
    crmv = models.CharField(max_length=20, unique=True, verbose_name="CRMV")
    telefone = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Telefone")

    class Meta:
        verbose_name = "Veterinário"
        verbose_name_plural = "Veterinários"

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.crmv})"
