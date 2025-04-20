from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista_produtos.html', {'produtos': produtos})


def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/formulario_produto.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'estoque/formulario_produto.html', {'form': form})

def alerta_estoque_baixo(request):
    produtos = Produto.objects.filter(estoque__lt=10)
    return render(request, 'estoque/alerta_estoque.html', {'produtos': produtos})
