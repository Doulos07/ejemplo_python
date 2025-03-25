def agregar_producto (productos) :
     nombre = input("ingrese nombre del producto: ")
     cantidad = int(input("ingrese cantidad: "))

     if nombre in productos :
         print("se actualiza el stock del producto")
         productos[nombre] += cantidad 
     else :
         print("se agrega el nuevo producto")
         productos[nombre] = cantidad
     # return None

def eliminar_producto (productos) :
     nombre = input("ingrese nombre del producto: ")
     if productos.get(nombre):  
         del productos[nombre]
         print("se elimino el producto")  
     else:  
         print("el producto no existe")
     # return None

def mostrar_inventario (productos) :
     for nombre, cantidad in productos.items() :
         print(f"{nombre} : {cantidad}")
     # return None

acciones = {
     1 : agregar_producto,
     2 : eliminar_producto,
     3 : mostrar_inventario
}

menu = [("agregar producto"), ("eliminar producto"), ("mostrar inventario"), ("salir")]
productos = {}

while True :
     #mostrar Menu
     for i, msj in enumerate(menu,1) :
         print (f"{i}. {msj}")
     #usuario ingresa una opciones
     opcion = int(input("ingrese una opciones: "))
     #sale del menu si seleciona opcion 4
     if opcion == 4 :
         break
     
     print()
     #ejecuta la accion
     accion = acciones.get(opcion)
     accion(productos)

     print()