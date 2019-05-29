# -*- coding: utf-8 -*-


empresas = []
def insertarEmpresas(empresas):
    salir=False
    while salir==False:
        empresa=[]
        nombre=input("Introduzca nombre:")
        apellidos=input("Introduzca apellidos:")
        dueno=input("Introduzca dueno:")
        antiguedad=input("Introduzca antiguedad:")
        cif=input("Introduzca iban:")
        pin=input("Introduzca pin:")
        balance=input("Introduzca balance:")
        oferta="No"
        empresa.append(nombre.title())
        empresa.append(apellidos.title())
        empresa.append(dueno.title())
        empresa.append(antiguedad)
        empresa.append(cif.title())
        empresa.append(pin)
        empresa.append(balance)
        empresa.append(oferta.upper())
        empresas.append(empresa)
        opcion = input("Desea introducir mas empresas S/N?")
        if opcion=='N':
            salir=True
        return empresas

def verEmpresa(cif,pin):
    for c in empresas:
        if c[2]==str(pin):
            if c[5]==str(pin):
                print("Empresa:\n")
                print("Nombre:"+c[0]+"\n")
                print("Dueño:"+c[1]+"\n")
                print("CIF:"+c[2]+"\n")
                print("Antiguedad:"+c[3]+" años\n")
                print("Cuenta IBAN:"+c[4]+"\n")
                print("PIN:"+c[5]+"\n")
                print("Balance:"+c[6]+" euros\n")
                print("Tiene oferta:"+c[7]+"\n")

def verEmpresas():
    for c in empresas:
        print("Empresa:\n")
        print("Nombre:"+c[0]+"\n")
        print("Dueño:"+c[1]+"\n")
        print("CIF:"+c[2]+"\n")
        print("Antiguedad:"+c[3]+" años\n")
        print("Cuenta IBAN:"+c[4]+"\n")
        print("PIN:"+c[5]+"\n")
        print("Balance:"+c[6]+" euros\n")
        print("Tiene oferta:"+c[7]+"\n")
