from django.contrib import admin
from .models import Producto,Estado_Producto,Categoria
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Estado_Producto)
