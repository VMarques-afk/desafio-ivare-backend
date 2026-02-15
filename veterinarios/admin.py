from django.contrib import admin
from .models import Veterinario


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'crmv', 'user')

    search_fields = ('nome', 'sobrenome', 'crmv')

    fieldsets = (
        ("Usuário Vinculado", {"fields": ("user",)}),
        ("Informações Pessoais", {"fields": ("nome", "sobrenome")}),
        ("Informações Profissionais", {"fields": ("crmv", "telefone")}),
    )


'''add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("usuario", "email", "nome", "sobrenome", "crmv", "password", "password_confirm"),
        }),
    )
    list_display = ('usuario', 'email', 'nome', 'sobrenome', 'crmv', 'is_staff')
    search_fields = ('usuario', 'email', 'crmv', 'nome', 'sobrenome')
    ordering = ('usuario',)'''
