# Tercera-pre-entrega
Repositorio del proyecto Django correspondiente a la tercera preentrega del curso de Python de CoderHouse

Proyecto en django cuyo objetivo final es generar una web que permita administrar las reparaciones, venta de 
máquinas y respuestos,  manuales y base de datos de clientes de un taller de reparación de máquinas herramientas.

Versión 0.1:
- Tabla de clientes con formulario de carga
- Tabla de ordenees de reparación con formulario de carga y consulta de reparaciones por nobre de cliente
- Tabla de manuales con formulario de carga
- Tabla de maquinas en venta con formulario de carga
- Tabla de repuestos en venta con formulario de carga

Todas la base de datos es de acceso público para la carga de información.
IMPORTANTE: No todas las clases poseen registros cargados pero se probaron los formularios de cada una. 
El html del formulario de carga es único cambiandose el form que levanta.

Mejoras deseadas pára proximas versiones:
- Generar 2 niveles de acceso, uno público para mostrar el contenido de la base de datos y otro privado para el CRUD de la misma
- Agregar a las tablas productos y repuestos un campo imagen que muestr el elementoi físico.
- Agregar a la tabla manuales un campo archivo para almacenar los mismos y permitir su descarga.
