from django.test import TestCase
from .models import Cliente

class ClienteTestCase(TestCase):
    def test_criacao_cliente(self):
        cliente = Cliente.objects.create(nome="João", email="joao@example.com")
        self.assertEqual(cliente.nome, "João")
