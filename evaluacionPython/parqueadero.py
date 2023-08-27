from carro import Carro
from parqueo import Parqueo
class Parqueadero():
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__listaParqueo=[]
        self.__listaCarro=[]
        self.__listaSalida=[]
        
    def getNombre(self):
        return self.__nombre
    def getListaParqueo(self):
        return self.__listaParqueo
    def getListaCarro(self):
        return self.__listaCarro
    def getListaSalida(self):
        return self.__listaSalida
        
    def registrarIngresoCarro(self, carro, fechaIngreso, puesto):
        self.__listaCarro.append(carro)
        parqueo=Parqueo(carro=carro,fechaIngreso=fechaIngreso,puesto=puesto)
        self.__listaParqueo.append(parqueo)
        
    def registrarSalidaCarro(self, placa, fechaSalida):
        verificacion=False
        lista=self.__listaParqueo
        for c in lista:
            contador=self.__listaParqueo.index(c)
            carro=c.getCarro()
            placa1=carro.getPlaca()
            color=carro.getColor()
            if placa==placa1:
                c.setFechaSalida(fechaSalida)
                self.__listaSalida.append([placa1, color, fechaSalida])
                self.__listaParqueo.pop(contador)
                verificacion=True               
        if verificacion==False:
            print("La placa del Carro no se encuentra en el Parqueadero")
            print()
        else:
            print("Carro Retirado correctamente")
            print()
                