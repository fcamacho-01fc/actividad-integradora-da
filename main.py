import produccion as prd
import ventas as vt
import clientes as cli
import inventario as inv
from menu import mostrar_menu


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            prd.menu_produccion()
        elif opcion == "2":
            vt.menu_ventas()
        elif opcion == "3":
            cli.menu_clientes()
        elif opcion == "4":
            inv.menu_inventario()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
