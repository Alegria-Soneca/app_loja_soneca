from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def site(request):
    return render(request, 'index.html')


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/adicionar_cliente.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/editar_cliente.html', {'form': form})

def deletar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'clientes/deletar_cliente.html', {'cliente': cliente})
