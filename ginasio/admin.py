from django.contrib import admin
from .models import PT, Membro, Sessao

class PTAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade",)
    search_fields = ("nome",)

class MembroAdmin(admin.ModelAdmin):
    list_display = ("nome", "email",)
    search_fields = ("nome",)

class SessaoAdmin(admin.ModelAdmin):
    list_display = ("pt", "membro", "data", "hora",)
    ordering = ("data", "hora",)
    search_fields = ("pt__nome", "membro__nome",)

admin.site.register(PT, PTAdmin)
admin.site.register(Membro, MembroAdmin)
admin.site.register(Sessao, SessaoAdmin)
