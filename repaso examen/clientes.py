# -*- coding: utf-8 -*-


clientes = []
def insertarClientes(clientes):
    salir=False
    while salir==False:
        cliente=[]
        nombre=input("Introduzca nombre:")
        apellidos=input("Introduzca apellidos:")
        dni=input("Introduzca dni:")
        antiguedad=input("Introduzca antiguedad:")
        iban=input("Introduzca iban:")
        pin=input("Introduzca pin:")
        balance=input("Introduzca balance:")
        oferta="No"
        cliente.append(nombre.title())
        cliente.append(apellidos.title())
        cliente.append(dni.title())
        cliente.append(antiguedad)
        cliente.append(iban.title())
        cliente.append(pin)
        cliente.append(balance)
        cliente.append(oferta.upper())
        clientes.append(cliente)
        opcion = input("Desea introducir mas clientes S/N?")
        if opcion=='N':
            salir=True
        if opcion=='s':
            insertarClientes(clientes)
        return clientes

def mostrarClientes(dni,pin):
    for c in clientes:  
        if c[2]==dni:
            if c[5]==str(pin):
                print("--------------------------------------------------\n")
                print("Clinte:\n")
                print("Nombre:"+c[0]+"\n")
                print("Apellidos:"+c[1]+"\n")
                print("DNI:"+c[2]+"\n")
                print("Antiguedad:"+c[3]+" años\n")
                print("Cuenta IBAN:"+c[4]+"\n")
                print("PIN:"+c[5]+"\n")
                print("Balance:"+c[6]+" euros\n")
                print("Tiene oferta:"+c[7]+"\n")
                print("--------------------------------------------------\n")

def mostrarClientes():
    for c in clientes:
        print("Clinte:\n")
        print("Nombre:"+c[0]+"\n")
        print("Apellidos:"+c[1]+"\n")
        print("DNI:"+c[2]+"\n")
        print("Antiguedad:"+c[3]+" años\n")
        print("Cuenta IBAN:"+c[4]+"\n")
        print("PIN:"+c[5]+"\n")
        print("Balance:"+c[6]+" euros\n")
        print("Tiene oferta:"+c[7]+"\n")


def borrar():
    salir=False
    i=0
    while salir==False:
        dni =input("Introduce el dni que queremos borrar:\n")
        for c in clientes:
            if dni.upper()==c[2]:
                print("Cliente encontrado.Procediendo a su borrado.....")
                clientes.pop(i)
            s=input("¿Desea borrar mas clientes?S/N\n")
            if s == 'n' or s=='N':
                salir=True
            i=i+1


def aplicarOferta():

    for c in clientes:
        if int(c[3]) >=3 and float(c[6])>=1500:
            if int(c[3])>=5 and float(c[6])>3000:
                if(c[3])>=10:
                    c[6]=c[6]+0.035*c[6]
                else:
                    c[6]=c[6]*0.02*c[6]
            c[6]=str(c[6])
            c[3]=str(c[3])

def comprobarCredenciales(dni,iban):
    salir = False
    if clientes != None:
        while salir == False:
            for c in clientes:
                if c[2] == dni.upper() and c[4] == iban.upper():
                    print("DNI y cuenta IBAN repetidos. Error.\n")
                else:
                    salir = True
