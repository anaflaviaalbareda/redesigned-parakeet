from django.core.validators import FileExtensionValidator
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categoria'

    def __str__(self):
        # return "name" from translation
        return self.nombre


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion')  # Field name made lowercase.
    short = models.CharField(db_column='Short', max_length=105)  # Field name made lowercase.
    foto = models.FileField(upload_to='img/productos', db_column='Foto', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])  # Field name made lowercase.
    destacado = models.BooleanField(db_column='Destacado', default=False)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio')  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=45)  # Field name made lowercase.
    categoria_1 = models.ForeignKey(Categoria, models.SET_NULL, db_column='Categoria 1', blank=True, null=True,related_name='categoria_1_Producto')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    categoria_2 = models.ForeignKey(Categoria, models.SET_NULL, db_column='Categoria 2', blank=True, null=True,related_name='categoria_2_Producto')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Producto'

    def __str__(self):
        # return "name" from translation
        return self.nombre
