from django.contrib import admin
from .models import Ingrediente, Receita, Utilizador

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)
    filter_horizontal = ("ingredientes",)

class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "email",)
    search_fields = ("nome",)
    filter_horizontal = ("favoritas",)

admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Utilizador, UtilizadorAdmin)
