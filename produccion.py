from datetime import date
import json


ARCHIVO_PRODUCCION = "datos/produccion.json"


def cargar_produccion():
    try:
        with open(ARCHIVO_PRODUCCION, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("El archivo de producción no tiene un formato válido.")
        return []


def guardar_produccion(registros):
    with open(ARCHIVO_PRODUCCION, "w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, ensure_ascii=False, indent=4)


def siguiente_id(registros):
    mayor_id = 0
    for registro in registros:
        if registro["id"] > mayor_id:
            mayor_id = registro["id"]
    return mayor_id + 1


def registrar_produccion():
    registros = cargar_produccion()
    try:
        cantidad = int(input("Huevos recolectados: "))
    except ValueError:
        print("Ingrese una cantidad numérica válida.")
        return

    registro = {
        "id": siguiente_id(registros),
        "fecha": date.today().isoformat(),
        "cantidad": cantidad
    }
    registros.append(registro)
    guardar_produccion(registros)
    print("Producción registrada.")


def listar_produccion():
    registros = cargar_produccion()
    if len(registros) == 0:
        print("No hay registros de producción.")
    for registro in registros:
        print("ID:", registro["id"], "Fecha:", registro["fecha"],
              "Cantidad:", registro["cantidad"])


def buscar_produccion():
    registros = cargar_produccion()
    try:
        registro_id = int(input("ID del registro: "))
    except ValueError:
        print("Ingrese un ID numérico válido.")
        return
    for registro in registros:
        if registro["id"] == registro_id:
            print(registro)
            return
    print("No se encontró el registro.")


def actualizar_produccion():
    registros = cargar_produccion()
    try:
        registro_id = int(input("ID del registro a actualizar: "))
    except ValueError:
        print("Ingrese un ID numérico válido.")
        return
    for registro in registros:
        if registro["id"] == registro_id:
            try:
                registro["cantidad"] = int(input("Nueva cantidad: "))
            except ValueError:
                print("Ingrese una cantidad numérica válida.")
                return
            guardar_produccion(registros)
            print("Registro actualizado.")
            return
    print("No se encontró el registro.")


def eliminar_produccion():
    registros = cargar_produccion()
    try:
        registro_id = int(input("ID del registro a eliminar: "))
    except ValueError:
        print("Ingrese un ID numérico válido.")
        return
    registros_nuevos = []
    encontrado = False
    for registro in registros:
        if registro["id"] == registro_id:
            encontrado = True
        else:
            registros_nuevos.append(registro)
    if encontrado:
        guardar_produccion(registros_nuevos)
        print("Registro eliminado.")
    else:
        print("No se encontró el registro.")


def menu_produccion():
    while True:
        print("\nPRODUCCIÓN")
        print("1. Registrar producción")
        print("2. Listar producción")
        print("3. Buscar registro")
        print("4. Actualizar registro")
        print("5. Eliminar registro")
        print("6. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_produccion()
        elif opcion == "2":
            listar_produccion()
        elif opcion == "3":
            buscar_produccion()
        elif opcion == "4":
            actualizar_produccion()
        elif opcion == "5":
            eliminar_produccion()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_produccion()
