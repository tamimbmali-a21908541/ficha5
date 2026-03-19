from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome

class Morada(models.Model):
    rua = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.rua}, {self.cidade}'

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    morada = models.OneToOneField(Morada, on_delete=models.CASCADE, related_name='cliente')

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente}'

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens_pedido')
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantidade}x {self.produto} (Pedido {self.pedido.id})'
