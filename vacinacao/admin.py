from django.contrib import admin
from .models import Usuario, Pet, Vacina, RegistroVacinacao

admin.site.register(Usuario)
admin.site.register(Pet)
admin.site.register(Vacina)
admin.site.register(RegistroVacinacao)
