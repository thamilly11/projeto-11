from django.contrib import admin
from django.utils.html import format_html
from .models import Aluno, Cidade, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_aluno', 'endereco', 'email', 'foto_thumbnail')
    fields = ('nome_aluno', 'endereco', 'email', 'foto', 'cidade', 'curso')
    
    def foto_thumbnail(self, obj):
        if obj.foto:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit: cover;" />',
                obj.foto.url
            )
        return "Sem foto"
    foto_thumbnail.short_description = 'Foto'

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla_estado',)

