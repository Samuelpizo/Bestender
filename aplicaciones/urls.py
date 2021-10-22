from django.urls import path
from . import views

urlpatterns = [
  #_______Proveedores__________________________________________________________
  path('',views.home),
  path('proveedores/principal/',views.principal),
  path('proveedores/',views.proveedores),
  path('registrarProveedor/',views.registrarProveedor),
  path('proveedores/edicionProveedor/<codigo>',views.edicionProveedor),
  path('editarProveedor/',views.editarProveedor),
  path('cancelar/',views.cancelar),
  path('proveedores/eliminarProveedor/<codigo>',views.eliminarProveedor),
  path('proveedores/transaccionitas/',views.transaccionitas),
  path('proveedores/producticos/',views.producticos),
  
  #________Transacciones_______________________________________________________
  path('transacciones/',views.transacciones),
  path('transacciones/volverini/',views.volverini),
  path('transacciones/creartransaccion/<codigoPrd>',views.creartransaccion),
  path('editarPrd/',views.editarPrd),
  path('transacciones/irProductos/',views.irProductos),
  path('transacciones/irProveedores/',views.irProveedores),
  
  #______Productos_____________________________________________________________
  path('productos/menu/',views.menu),
  path('productos/',views.productos),
  path('registrarProducto/',views.registrarProducto),
  path('productos/edicionProducto/<codigoPrd>',views.edicionProducto),
  path('editarProducto/',views.editarProducto),
  path('productos/eliminarProducto/<codigoPrd>',views.eliminarProducto),
  path('productos/formProducto/',views.formProducto),
  path('productos/formProducto/volverPrd/',views.volverPrd),
  path('productos/volver/',views.volver),
  path('productos/iraProveedores/',views.iraProveedores),
  path('productos/iraTransacciones/',views.iraTransacciones),
  path('productos/edicionProducto/volverPrd/',views.volverPrd),
 
  #path('productos/iraTransacciones/',views.iraTransacciones),
]