from datetime import date
import json


ARCHIVO_INVENTARIO = "datos/inventario.json"


def cargar_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("El archivo " + ruta + " no tiene un formato válido.")
        return None


def calcular_total(registros):
    total = 0
    for registro in registros:
        total += registro["cantidad"]
    return total


def guardar_inventario(inventario):
    with open(ARCHIVO_INVENTARIO, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, ensure_ascii=False, indent=4)


def crear_inventario():
    produccion = cargar_json("datos/produccion.json")
    ventas = cargar_json("datos/ventas.json")
    if produccion is None:
        produccion = []
    if ventas is None:
        ventas = []

    total_producido = calcular_total(produccion)
    total_vendido = calcular_total(ventas)
    inventario = {
        "ultima_actualizacion": date.today().isoformat(),
        "total_producido": total_producido,
        "total_vendido": total_vendido,
        "existencia": total_producido - total_vendido
    }
    guardar_inventario(inventario)
    return inventario


def inicializar_inventario():
    inventario = cargar_json(ARCHIVO_INVENTARIO)
    if inventario is None:
        inventario = crear_inventario()
    return inventario


def mostrar_inventario():
    inventario = inicializar_inventario()
    print("Última actualización:", inventario["ultima_actualizacion"])
    print("Total producido:", inventario["total_producido"])
    print("Total vendido:", inventario["total_vendido"])
    print("Existencia:", inventario["existencia"])


def actualizar_inventario():
    inventario = crear_inventario()
    print("Inventario reconstruido.")
    print("Existencia:", inventario["existencia"])


def menu_inventario():
    while True:
        print("\nINVENTARIO")
        print("1. Consultar inventario")
        print("2. Reconstruir / actualizar inventario")
        print("3. Mostrar resumen")
        print("4. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            actualizar_inventario()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_inventario()
