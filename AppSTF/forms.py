from django import forms

class OrdenesFormulario(forms.Form):
    opcionesEstado = [('IN','Ingresado'),
                      ('RE','Revisado'),
                      ('PR','PResupuestado'),
                      ('AC','Aceptado'),
                      ('NC','Rechazado'),
                      ('RP','Reparado'),
                      ('RT','Retirado'),
                      ]   
    estado = forms.ChoiceField(choices=opcionesEstado)
    cliente = forms.CharField()
    tipo = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    obs = forms.CharField()
    presupuesto = forms.FloatField()

class MaquinasFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    tipo = forms.CharField(max_length=60)
    marca = forms.CharField(max_length=60)
    modelo = forms.CharField(max_length=60)
    desc = forms.CharField(max_length=400)
    precio = forms.DecimalField()
    stock = forms.IntegerField()
    #foto = forms.ImageField()

class RepuestosFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    marca = forms.CharField(max_length=60)
    modelo = forms.CharField(max_length=60)
    precio = forms.FloatField()
    stock = forms.IntegerField()
    
class ManualesFormulario(forms.Form):
    tipo = forms.CharField()
    marca = forms.CharField()
    modelo = forms.CharField()
    
class ClientesFormulario(forms.Form):
    razonSocial = forms.CharField()
    cuit = forms.IntegerField()
    contacto = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    direccion = forms.CharField()