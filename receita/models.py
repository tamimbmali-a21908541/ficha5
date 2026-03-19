from django.db import models

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    ingredientes = models.ManyToManyField(Ingrediente, related_name='receitas')

    def __str__(self):
        return self.nome

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    favoritas = models.ManyToManyField(Receita, related_name='utilizadores_favoritos', blank=True)

    def __str__(self):
        return self.nome
