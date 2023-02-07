from django.urls import path
from AppSTF import views

urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('nosotros', views.sobre, name="Nosotros"),
    path('maquinas', views.maquinasFormulario, name="Maquinas"),
    path('ordenes', views.ordenesFormulario, name="Reparaciones"),
    path('repuestos', views.repuestosFormulario, name="Repuestos"),
    path('manuales', views.manualesFormulario, name="Manuales"),
    path('clientes', views.clientesFormulario, name="Clientes"),
    path('buscar', views.buscarOrdenes, name="Buscar"),
    path('resultadorden/', views.resultadoOrden),
]