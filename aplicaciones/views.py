from django.shortcuts import redirect, render
from .models import proveedor
from django.contrib import messages
from .models import producto

# Create your views here.

def home (request):
    
    return render(request,"gestionProveedor.html")

def principal (request):
    return redirect('/')   

def proveedores (request):
    listadoProveedores = proveedor.objects.all()
    
    return render(request,"proveedores.html",{"proveedores": listadoProveedores})


def registrarProveedor(request):
    codigo=request.POST['txtcodigo'] 
    nombre=request.POST['txtnombre']
    telefono = request.POST['txttelefono']
    gmail = request.POST['txtgmail']
    direccion = request.POST['txtdireccion']  

    proveedores = proveedor.objects.create( codigo=codigo, nombre=nombre, telefono=telefono, gmail=gmail, direccion=direccion)
    messages.success(request, '¡Proveedor registrado!')
    return redirect('/proveedores/')   

def edicionProveedor(request,codigo):
    proveedores = proveedor.objects.get(codigo=codigo)
    return render(request,"edicionProveedor.html",{"proveedores": proveedores})

def editarProveedor(request):
    codigo=request.POST['txtcodigo'] 
    nombre=request.POST['txtnombre']
    telefono = request.POST['txttelefono']
    gmail = request.POST['txtgmail']
    direccion = request.POST['txtdireccion'] 

    proveedores = proveedor.objects.get(codigo=codigo)
    proveedores.nombre = nombre
    proveedores.telefono = telefono
    proveedores.gmail = gmail
    proveedores.direccion = direccion
    proveedores.save()
    messages.success(request, '¡Proveedor modificado!')
    return redirect('/proveedores/')



def eliminarProveedor (request,codigo):
    proveedores = proveedor.objects.get(codigo=codigo)
    proveedores.delete()
    messages.success(request, '¡Proveedor eliminado!')
    return redirect('/proveedores/')

def cancelar(request):
    return redirect('/proveedores/')  

#____________________________________________________Transacciones__________________________________________

def transacciones (request):
    listadoProductos = producto.objects.all()
    return render (request,"transacciones.html",{"productos": listadoProductos}) 

def creartransaccion (request,codigoPrd):
    productos = producto.objects.get(codigoPrd=codigoPrd)
    return render(request,"crearTransaccion.html",{"productos": productos})

def editarPrd(request):
    codigoPrd=request.POST['txtcodigoPrd'] 
    nombre = request.POST['txtnombre']
    tipodeTransaccion = request.POST['txtTransaccion']
    cantidadA = request.POST['cantidadA'] 
    cantidadB = request.POST['cantidadB'] 
    fecha = request.POST['txtfecha'] 

    #if tipodeTransaccion == "compra":
        #cantidad = cantidadA+cantidadB
    #else: 
        #cantidad= cantidadA-cantidadB    



    productos = producto.objects.get(codigoPrd=codigoPrd)
    productos.codigoPrd= codigoPrd
    
    productos.nombre = nombre
    productos.tipodeTransaccion=tipodeTransaccion
    productos.cantidadA=cantidadA
    productos.cantidadB=cantidadB
    productos.fecha=fecha
    
    productos.save()
    messages.success(request, '¡Producto modificado!')
    return redirect('/transacciones/')


#____________________________________________________Productos______________________________________________   

def menu (request):
    return redirect('/') 


def productos (request):
    listadoProductos = producto.objects.all()
    listadoProveedores= proveedor.objects.all()
    return render (request,"productos.html",{"productos": listadoProductos})

def edicionProducto(request,codigoPrd):
    productos = producto.objects.get(codigoPrd=codigoPrd)
    return render(request,"edicionProducto.html",{"productos": productos}) 

def editarProducto(request):
    codigoPrd=request.POST['txtcodigoPrd'] 
    #codigo=request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    categoria = request.POST['txtcategoria']
    descripcion = request.POST['txtdescripcion']  

    productos = producto.objects.get(codigoPrd=codigoPrd)
    productos.codigoPrd= codigoPrd
    #productos.codigo= codigo
    productos.nombre = nombre
    productos.categoria=categoria
    productos.descripcion=descripcion
    
    productos.save()
    messages.success(request, '¡Producto modificado!')
    return redirect('/productos/')

def eliminarProducto (request,codigoPrd):
    productos = producto.objects.get(codigoPrd=codigoPrd)
    productos.delete()
    messages.success(request, '¡Producto eliminado!')
    return redirect('/productos/')    

def registrarProducto(request):
    
    codigoPrd=request.POST['txtcodigoPrd'] 
    #codigo=request.POST['txtcodigo']
    #nombreP=request.POST['txtnombreP']
    nombre = request.POST['txtnombre']
    categoria = request.POST['txtcategoria']
    descripcion = request.POST['txtdescripcion']
     
    productos = producto.objects.create( codigoPrd=codigoPrd,descripcion=descripcion,nombre=nombre, categoria=categoria)
    #proveedores= proveedor.objects.create(codigo=codigo,nombre=nombreP)
    messages.success(request, '¡Producto registrado!')
    return redirect('/productos/') 

def formProducto(request):  
    return render(request,"creacionProducto.html")  

#___________________________________________________

def volverini (request):
    return redirect('/')

def volverPrd (request):
    return redirect('/productos/') 
#############################    

def volver (request):
    return redirect('/')

def iraProveedores(request):
    return redirect('/proveedores/')

def iraTransacciones(request):
    return redirect('/transacciones/')

def irProductos(request):
    return redirect('/productos/')

def irProveedores(request):
    return redirect('/proveedores/')

def producticos(request):
    return redirect('/productos/')    

def transaccionitas(request):
    return redirect('/transacciones/')   

   

#############################





#__________________________________________________

