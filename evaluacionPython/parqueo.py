from carro import Carro
class Parqueo():
    def __init__(self,carro=None,fechaIngreso=None,fechaSalida=None,puesto=int):
        self.__carro=carro
        self.__fechaIngreso=fechaIngreso
        self.__fechaSalida=fechaSalida
        self.__puesto=puesto
        
    def getCarro(self):
        return self.__carro
    def getFechaIngreso(self):
        return self.__fechaIngreso
    def getFechaSalida(self):
        return self.__fechaSalida
    def getPuesto(self):
        return self.__puesto
    
    def setCarro(self,carro):
        self.__carro=carro
    def setFechaIngreso(self,fechaIngreso):
        self.__fechaIngreso=fechaIngreso
    def setFechaSalida(self,fechaSalida):
        self.__fechaSalida=fechaSalida
    def setPuesto(self,puesto):
        self.__puesto=puesto