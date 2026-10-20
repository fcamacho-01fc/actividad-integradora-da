from datetime import date
import json


ARCHIVO_VENTAS = "datos/ventas.json"


def cargar_ventas():
    try: 
        with open(ARCHIVO_VENTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("Ha ocurrido un error, no existe el archivo")
        return [];
    except json.JSONDecodeError:
        print("Ha ocurrido un error al decodificar el json")


def guardar_ventas(registros):
    try:
        with open(ARCHIVO_VENTAS, "w", encoding="utf-8") as archivo:
            json.dump(registros, archivo)
    except e:
        print("Ha ocurrido un error al guardar el archivo: ",e)


def siguiente_id(registros):
    last_id = 0
    for registro in registros:
        if registro["id"] > last_id:
            last_id = registro["id"]
    return last_id+1


def registrar_venta():
    registros = cargar_ventas()
    try:
        cantidad = int(input("Huevos vendidos: "))
        precio = float(input("Precio por producto: "))
    except ValueError:
        print("Ingrese datos validos numericos")
        return
    cliente_id = None
    id_cliente = input("Ingrese id del cliente (opcional): ")
    if id_cliente != "": 
         
      try:
          cliente_id = int(id_cliente)
      except ValueError:
           print("Id del cliente debe ser numerico, el registro de la venta sera sin cliente")
           cliente_id = None
      else: 
        import clientes
        clientes_registrados = clientes.cargar_clientes();
        cliente_existente = False
        for cliente in clientes_registrados:
            if cliente["id"] == cliente_id:
                cliente_existente = True
        if not cliente_existente:
            print("No existe el cliente, el registro se hara sin cliente")
            cliente_id = None
    
    venta = {
        "id":siguiente_id(registros),
        "cantidad": cantidad,
        "precio":precio,
        "fecha": date.today().isoformat(),
        "cliente": cliente_id
    }

    registros.append(venta)
    guardar_ventas(registros)
    print("Venta guardada")
            

def listar_ventas():
    registros = cargar_ventas()
    if len(registros)==0:
        print("No hay ventas")
    else: 
        for venta in registros:
            total = venta["cantidad"]*venta["precio"]
            print(
                "ID:", venta["id"],
                "cantidad: ", venta["cantidad"],
                "precio: ", venta["precio"],
                "fecha: ", venta["fecha"],
                "cliente: ", venta["cliente"],
                "total de la venta: ", total
            )


def buscar_venta():
    pass


def actualizar_venta():
    registros = cargar_ventas()
    try: 
        venta_id = int(input("Ingrese id de venta a modificar: "))
    except ValueError:
        print("Ingrese dato valido de id numerico")
        return
    for venta in registros:
        if venta["id"] == venta_id:
            try:
                cantidad = int(input("Ingrese nueva cantidad: "))
                precio = float(input("Ingrese nuevo precio: "))
            except ValueError:
                print("Ingrese valor numerico valido")
                return
            venta["cantidad"] = cantidad
            venta["precio"] = precio
            guardar_ventas(registros)
            print("Venta actualizada")
            return



def eliminar_venta():
    pass


def menu_ventas():
    while True:
        print("\nVENTAS")
        print("1. Registrar venta")
        print("2. Listar ventas")
        print("3. Buscar venta")
        print("4. Actualizar venta")
        print("5. Eliminar venta")
        print("6. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            listar_ventas()
        elif opcion == "3":
            buscar_venta()
        elif opcion == "4":
            actualizar_venta()
        elif opcion == "5":
            eliminar_venta()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_ventas()
