from django.urls import path
from . import views

urlpatterns = [

    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('estoque/alerta/', views.alerta_estoque_baixo, name='alerta_estoque'),
    path('produtos/', views.lista_produtos, name='lista_produtos'), 
]
