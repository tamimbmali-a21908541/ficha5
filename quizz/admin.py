from django.contrib import admin
from .models import Quiz, Pergunta, Opcao, Participante, Tentativa

class OpcaoInline(admin.TabularInline):
    model = Opcao
    extra = 4

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ("texto", "quiz",)
    search_fields = ("texto",)
    inlines = [OpcaoInline]

class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ("titulo",)
    inlines = [PerguntaInline]

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email",)
    search_fields = ("nome",)

class TentativaAdmin(admin.ModelAdmin):
    list_display = ("participante", "quiz", "data", "pontuacao",)
    ordering = ("-data",)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Opcao)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Tentativa, TentativaAdmin)
