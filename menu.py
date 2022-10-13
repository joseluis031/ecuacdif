import os
import helpers
import Clase.ejercicio as ej


def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido a Ecuaciones dif  ")
        print("========================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2   ")
        print("[3] Ejercicio 3   ")
        print("[4] Ejercicio 4")
        print("[5] Cerrar la clase de ecuaciones   ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Enunciado del ejercicio 1...\n")
            import sympy as sp
            from Clase.ejercicio import Ecuacion1
            x = sp.Symbol("x")
            y = sp.Function("y")

            a = y(x).diff(x)
            sol1 = Ecuacion1(x,y,a)
            print(sol1)
            sol1.resolver()

        elif opcion == '2':
            print("Buscando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")

        elif opcion == '3':
            print("Añadiendo un cliente...\n")

            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        elif opcion == '4':
            print("Modificando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(
                    2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(
                    2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '5':
            print("Borrando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
            print("Cliente borrado correctamente.") if db.Clientes.borrar(
                dni) else print("Cliente no encontrado.")

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")