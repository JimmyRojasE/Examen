from django import forms
from .models import Producto, Estado_Producto, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields='__all__'
class EstadoProductoForm(forms.ModelForm):
    class Meta:
        model=Estado_Producto
        fields='__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model =User
        fields=['username','first_name','last_name','email','password1','password2']

