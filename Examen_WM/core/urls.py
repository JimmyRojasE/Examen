from django.urls import path
from .views import home,ver_producto,ver_categoria, form_producto,listar_producto,editar_producto,eliminar_producto,registro,ver_lista_producto
urlpatterns = [
    path('', home,name='home'),
    path('form-producto', form_producto,name='form_producto'),
    path('listar-producto', listar_producto,name='listar_producto'),
    path('editar-producto/<id>', editar_producto,name='editar_producto'),
    path('eliminar-producto/<id>', eliminar_producto,name='eliminar_producto'),
    path('registro/', registro,name='registro'),
    path('listar-productos', ver_lista_producto,name='ver_lista_producto'),
    path('ver-producto/<id>', ver_producto,name='ver_producto'),
    path('ver-categoria/<id>', ver_categoria,name='ver_categoria'),
   
    
]