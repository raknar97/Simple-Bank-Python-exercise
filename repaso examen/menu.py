# -*- coding: utf-8 -*-
import clientes as c
import empresas as e
import banco as b
def menu():
    '''print("CLIENTES\n")
    c.insertarClientes(c.clientes)
    print("EMPRESAS\n")
    e.insertarEmpresas(e.empresas)'''
    salir = False
    while salir==False:
        print("***Bienvenidos al Banco Sol ***\n")
        opcion =input("Por favor, identifiquese como ciente,empresa o administrador:\n")
        if opcion=="cliente":
            dni=input("Introduzca DNI:")
            pin=input("Introduzca PIN:")
            c.mostrarClientes(dni,pin)
        elif opcion=="empresa":
            cif=input("Introduzca CIF:")
            pin=input("Introduzca PIN:")
            e.verEmpresas(cif,pin)
        elif opcion=="admin":
            b.menuBanco()
        elif opcion=="salir":
            print("Saliendo.....\n")
            salir=True
        else:
            print("No ha introducido ninguna opcion correcta\n")
menu()