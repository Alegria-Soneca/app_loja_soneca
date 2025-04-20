from django.db import models

# Create your models here.


class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('Administrador', 'Administrador'),
        ('Usuário', 'Usuário'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def __str__(self):
        return self.nome
