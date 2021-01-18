from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=20)
    estado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name='rol'
        verbose_name_plural='roles'

    def _str_(self):
        return self.nombre


class Direccion(models.Model):
    nombre = models.CharField(max_length=80)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name='direccion'
        verbose_name_plural='direcciones'

    def _str_(self):
        return self.nombre

class Category(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        
        verbose_name='category'
        verbose_name_plural='categorys'

    def _str_(self):
        return self.nombre


class Usuario(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
      
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def _str_(self):
        return self.email
        

class Product (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    imagen = models.ImageField(upload_to='productos', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    peso = models.IntegerField()
    medida = models.CharField(max_length=30)
    estado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name='product'
        verbose_name_plural='products'

    def _str_(self):
        return self.nombre


class List (models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
 
    class Meta:
        
        verbose_name='list'
        verbose_name_plural='lists'

    def _str_(self):
        return self.nombre

class client(models.Model):
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=9)
    direcciones = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lists = models.ForeignKey(List, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    class Meta:
        
        verbose_name='client'
        verbose_name_plural='clients'

    def _str_(self):
        return self.nombre