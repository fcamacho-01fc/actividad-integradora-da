def cargar_clientes():
    pass


def guardar_clientes(clientes):
    pass


def siguiente_id(clientes):
    pass


def registrar_cliente():
    pass


def listar_clientes():
    pass


def buscar_cliente():
    pass


def actualizar_cliente():
    pass


def eliminar_cliente():
    pass


def menu_clientes():
    while True:
        print("\nCLIENTES")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("6. Regresar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            actualizar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_clientes()
