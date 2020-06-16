from django.contrib import admin
from .models import ConfiabilidadeEmpresa

# Register your models here.


class ConfiabilidadeEmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'indice')


admin.site.register(ConfiabilidadeEmpresa, ConfiabilidadeEmpresaAdmin)
