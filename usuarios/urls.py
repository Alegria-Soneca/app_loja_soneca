from django.urls import path
from . import views

urlpatterns = [
    path('criar/', views.criar_usuario, name='criar_usuario'),
    path('listar/', views.listar_usuarios, name='listar_usuarios'),
    path('excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
]
