from django.contrib import admin
from .models import Turma, Professor, Aluno

class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "turma",)
    search_fields = ("nome",)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_nascimento", "turma",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aluno, AlunoAdmin)
