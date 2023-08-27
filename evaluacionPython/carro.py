class Carro():
    def __init__(self,placa, color):
        self.__placa=placa
        self.__color=color
        
    def getPlaca(self):
        return self.__placa
    def getColor(self):
        return self.__color
    
    def setPlaca(self,placa):
        self.__placa=placa
    def setColor(self,color):
        self.__color=color