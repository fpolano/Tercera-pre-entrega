from django.db import models

# Create your models here.

class Ordenes(models.Model):
    opcionesEstado = [('IN','Ingresado'),
                      ('RE','Revisado'),
                      ('PR','PResupuestado'),
                      ('AC','Aceptado'),
                      ('NC','Rechazado'),
                      ('RP','Reparado'),
                      ('RT','Retirado'),
                      ]
    estado = models.CharField(max_length = 2,choices = opcionesEstado,default = 'IN')
    fechaIngreso = models.DateField(auto_now_add = True)
    cliente = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    obs = models.TextField(max_length=300)
    presupuesto = models.FloatField(blank = True)
    
    def __str__(self):
        return f"Cliente: {self.cliente}; Máquina:{self.tipo};Fecha ingreso: {self.fechaIngreso}; Estado: {self.estado}"

class Maquinas(models.Model):
    nombre = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    desc = models.TextField(max_length=400)
    precio = models.FloatField()
    stock = models.SmallIntegerField()
    #foto = models.ImageField()


    def __str__(self):
        return f"{self.nombre} Marca:{self.marca} Modelo:{self.modelo} precio: ${self.precio}"

class Repuestos(models.Model):
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    precio = models.FloatField()
    stock = models.SmallIntegerField()
    #foto = models.ImageField()

    def __str__(self):
        return f"{self.nombre} Marca:{self.marca} Modelo:{self.modelo} precio: ${self.precio}"    

class Manuales(models.Model):
    tipo = models.CharField(max_length=60)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    # archivo = models.FileField()

    def __str__(self):
        return f"Manual de {self.tipo} marca:{self.marca} modelo:{self.modelo}"   
    
class Clientes(models.Model):
    razonSocial = models.CharField(max_length=60)
    cuit = models.PositiveSmallIntegerField(blank = True)
    contacto = models.CharField(max_length=60,blank=True)
    email = models.EmailField()
    telefono = models.PositiveSmallIntegerField()
    direccion = models.CharField(max_length=100,blank = True)
    
    def __str__(self):
        return f"{self.razonSocial} cuit: {self.cuit}"   