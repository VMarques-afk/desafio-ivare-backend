from django.contrib import admin
from django import forms
from .models import Veterinario
from vacinacao.models import Usuario


class VeterinarioForm(forms.ModelForm):
    username_customizado = forms.CharField(
        label="Username de Acesso",
        required=False,
        help_text="Digite o login (ex: fulano.vet). Se já houver um usuário, ignore este campo."
    )

    class Meta:
        model = Veterinario
        fields = '__all__'


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    form = VeterinarioForm
    list_display = ('nome', 'sobrenome', 'crmv', 'user')
    search_fields = ('nome', 'sobrenome', 'crmv')

    fieldsets = (
        ("Configuração de Acesso", {
            "fields": ("username_customizado", "user"),
            "description": "Crie um novo username ou selecione um Usuário existente."
        }),
        ("Informações Pessoais", {
            "fields": ("nome", "sobrenome")
        }),
        ("Informações Profissionais", {
            "fields": ("crmv", "telefone")
        }),
    )

    def save_model(self, request, obj, form, change):
        username_novo = form.cleaned_data.get('username_customizado')

        if username_novo and not obj.user:
            usuario_criado = Usuario.objects.create_user(
                username=username_novo,
                password='mudar123'
            )
            obj.user = usuario_criado

        super().save_model(request, obj, form, change)
