from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    categoria=Categoria.objects.all()
    datos={
        'Categoria':categoria
    }
    return render(request,'core/home.html',datos)

def form_producto(request):
    data={
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario= ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente"
        else:
            data['form']=formulario


    return render(request,'core/formularios/form_producto.html',data)
def listar_producto(request):

    listarproducto = Producto.objects.all

    data = {
        'listarproducto' : listarproducto
    }

    return render(request, 'core/paginas/listar_productos.html', data)
def ver_lista_producto(request):

    listarproducto = Producto.objects.all

    data = {
        'listarproducto' : listarproducto
    }

    return render(request, 'core/paginas/ver_lista_productos.html', data)

def editar_producto(request, id):
    
    producto= get_object_or_404(Producto,id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data['form']=formulario
    return render(request, 'core/paginas/editar_producto.html', data)

def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect(to="listar_producto")

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method=='POST':
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data['form']=formulario

    return render(request, 'registration/registro.html', data)

def ver_producto(request, id):
    
    producto= get_object_or_404(Producto,id=id)

    data = {
        'producto' : producto
    }

    return render(request, 'core/paginas/ver_producto.html', data)

def ver_categoria(request, id):
    
    producto= Producto.objects.filter(id_categoria_id=id)

    data = {
        'listarproducto' : producto
    }

    return render(request, 'core/paginas/ver_prod_cat.html', data)    


    