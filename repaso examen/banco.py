# -*- coding: utf-8 -*-
import clientes as c
import empresas as e
def menuBanco():
    salir = False
    while salir == False:
        print("--- Menú Banco ---\n")
        print("1. Ver clientes o empresas\n")
        print("2. Insertar clientes\n")
        print("3. Eliminar clientes\n")
        print("4. Ver y aplicar ofertas para clientes y/o empresas\n")
        print("5. Salir\n")
        o = int(input("Elija opcion:"))
        if o == 1:
            print("VER CLIENTES O EMPRESAS\n")
            op = input("Introduce clientes o empresas para mostrar:")
            mostrar(op)
        elif o == 2:
            print("INSERTAR CLIENTES\n")
            c.insertarClientes(c.clientes)
        elif o == 3:
            print("ELIMINAR CLIENTES\n")
            c.borrar()
        elif o == 4:
            print("VER Y APLICAR OFERTAS\n")
            c.aplicarOfertas()
        elif o == 5:
            print("Saliendo...\n")
            salir = True
        else:
            print("No ha introducido ninguna opcion correcta. Vuelva a intentarlo.\n")

def mostrar(opcion):
    if opcion == "clientes":
        c.mostrarClientes()
    elif opcion=="empresas":
        e.verEmpresas()
    else:
        print("No ha introducido ni clientes ni empresas. Error.")


