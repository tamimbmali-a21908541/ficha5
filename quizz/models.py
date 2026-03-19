from django.db import models

class Quiz(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.TextField()

    def __str__(self):
        return self.texto[:50]

class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='opcoes')
    texto = models.CharField(max_length=200)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Tentativa(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='tentativas')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='tentativas')
    data = models.DateTimeField(auto_now_add=True)
    pontuacao = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.participante} - {self.quiz} ({self.pontuacao} pts)'
