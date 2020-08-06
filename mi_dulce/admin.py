from django.contrib import admin
from .models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','idcategoria','descripcion')

admin.site.register(Categoria,CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','idproducto','short','destacado','precio')
    list_filter = ('destacado',)
    search_fields = ('nombre', 'short', 'descripcion','idproducto', )

admin.site.register(Producto,ProductoAdmin)
