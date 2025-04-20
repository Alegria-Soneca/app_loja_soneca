from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='lista_categorias'),
    path('nova/', views.nova_categoria, name='nova_categoria'),
    path('editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
]
