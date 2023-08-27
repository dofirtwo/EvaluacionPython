from carro import Carro
from parqueadero import Parqueadero
from datetime import datetime

parqueadero=Parqueadero("Lavaopita")

def registarIngreso():
    verificacion=True
    placa=input("Ingrese la placa del carro: ")
    color= input("Ingrese el color del carro: ")
    carro=Carro(placa,color)
    puesto=int(input("Ingrese el  puesto del carro en el parqueadero: "))
    for p1 in parqueadero.getListaParqueo():
            if puesto==p1.getPuesto():
                verificacion=False
                break
    if verificacion == False:
        print()
        print("OCUPADO")
        print()
    elif puesto>20 or puesto<=0:
        print()
        print("Solo hay 20 Puestos en el parqueadero")
        print()
    else:
        print()
        print("DISPONIBLE")
        print()
        parqueadero.registrarIngresoCarro(carro,datetime.now(),puesto)
  
def registrarSalida():
    placa=input("Ingrese la placa del carro: ")
    parqueadero.registrarSalidaCarro(placa, datetime.now())

def ListarParqueo():
    print("Carros que aun permanecen en el Parqueadero: ")
    for p in parqueadero.getListaParqueo():
        carro=p.getCarro()
        print(f"Placa: {carro.getPlaca()}, Color: {carro.getColor()}, Fecha Ingresado: {p.getFechaIngreso()}, Puesto: {p.getPuesto()}")
    print() 
        
def ListarSalida():
    print("Carros que ya han sido retirados del Parqueadero")
    for s in parqueadero.getListaSalida():
        print(f"Placa: {s[0]}, Color: {s[1]} Fecha Salida: {s[2]}")
    print()

def ListarPorPuesto():
    verficiacion=False
    puesto=int(input("Ingrese el  puesto del Carro que quiere consultar: "))
    for p in parqueadero.getListaParqueo():
        carro=p.getCarro()
        if puesto==p.getPuesto():
            print(f"el carro ubicado en el Puesto: {p.getPuesto()} tiene las sigientes caracteristicas: ")
            print(f"Placa: {carro.getPlaca()}, Color: {carro.getColor()}, Hora de Ingreso: {p.getFechaIngreso()}")
            verficiacion=True
    if verficiacion==False:
        print("Ningun carro se encuentra en ese puesto")    
x=0
while x!=5:
    print(f"\t\t Bienvenido a {parqueadero.getNombre()}")
    print("\t1. Registrar Ingreso")
    print("\t2. Registrar salida")
    print("\t3. Consultar Todos carros")
    print("\t4. Consultar carro por Puesto en el Parqueadero")
    print("\t5. salir")
    x= int(input("\tIngrese la opcion (1-5): "))
    if x==1:
        registarIngreso()
    if x==2:
        registrarSalida()
    if x==3:
        ListarParqueo()
        ListarSalida()
    if x==4:
        ListarPorPuesto()
    