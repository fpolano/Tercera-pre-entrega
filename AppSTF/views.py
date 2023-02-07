from django.shortcuts import render
from AppSTF.forms import *
from AppSTF.models import *

# Create your views here.
def inicio(request):
    return render(request,"AppSTF/index.html")

def sobre(request):
    return render(request,"AppSTF/about.html")

def ordenesFormulario(request):
    if request.method == "POST":
 
        miFormulario = OrdenesFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            orden = Ordenes(estado = informacion["estado"],
                            cliente = informacion["cliente"],
                            tipo = informacion["tipo"],
                            marca =informacion["marca"],
                            modelo = informacion["modelo"],
                            obs = informacion["obs"],
                            presupuesto = informacion["presupuesto"],
                            )
            orden.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = OrdenesFormulario()
 
    return render(request, "AppSTF/carga.html", {"miFormulario": miFormulario})

def maquinasFormulario(request):
    if request.method == "POST":
 
        miFormulario = MaquinasFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            maquina = Maquinas(nombre = informacion["nombre"],
                                tipo = informacion["tipo"],
                                marca = informacion["marca"],
                                modelo = informacion["modelo"],
                                desc = informacion["desc"],
                                precio = informacion["precio"],
                                stock = informacion["stock"],
                                )
                  #             foto = informacion["foto"],
            maquina.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = MaquinasFormulario()
 
    return render(request, "AppSTF/carga.html", {"miFormulario": miFormulario})
    
def repuestosFormulario(request):
    if request.method == "POST":
 
        miFormulario = RepuestosFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            repu = Repuestos(nombre = informacion["nombre"],
                            marca = informacion["marca"],
                            modelo =informacion["modelo"],
                            precio = informacion["precio"],
                            stock = informacion["stock"],
                            )
            repu.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = RepuestosFormulario()
 
    return render(request, "AppSTF/carga.html", {"miFormulario": miFormulario})

def manualesFormulario(request):
    if request.method == "POST":
 
        miFormulario = ManualesFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            manual = Manuales(tipo = informacion["tipo"],
                            marca = informacion["marca"],
                            modelo =informacion["modelo"],
                            )
            manual.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = ManualesFormulario()
 
    return render(request, "AppSTF/carga.html", {"miFormulario": miFormulario})

def clientesFormulario(request):
    if request.method == "POST":
 
        miFormulario = ClientesFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = Clientes(razonSocial= informacion["razonSocial"],
                                cuit = informacion["cuit"],
                                contacto = informacion["contacto"],
                                email =informacion["email"],
                                telefono = informacion["telefono"],
                                direccion= informacion["direccion"],
                                )
            cliente.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = ClientesFormulario()
 
    return render(request, "AppSTF/carga.html", {"miFormulario": miFormulario})

def buscarOrdenes(request):
    return render(request,"AppSTF/buscarorden.html")

def resultadoOrden(request):
    if request.GET["cliente"]:
        cliente = request.GET["cliente"]
        reparaciones = Ordenes.objects.filter(cliente__icontains=cliente)
        return render(request,"AppSTF/buscarorden.html",{"ordCliente":reparaciones})
    else:
        respuesta = "Sin datos"
        return render(request,"AppSTF/buscarorden.html",{"respuesta":respuesta})