from django.contrib import admin
from .models import Categoria, Produto, Morada, Cliente, Pedido, ItemPedido

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "categoria",)
    ordering = ("nome",)
    search_fields = ("nome",)

class MoradaAdmin(admin.ModelAdmin):
    list_display = ("rua", "cidade", "codigo_postal",)
    search_fields = ("cidade",)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "morada",)
    search_fields = ("nome",)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data",)
    ordering = ("-data",)
    search_fields = ("cliente__nome",)
    inlines = [ItemPedidoInline]

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade",)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Morada, MoradaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
