from .base_datos import Entidad

class Vehiculo(Entidad):
    def __init__(self, placa, modelo):
        super().__init__(placa)
        self.__modelo = modelo

    def placa(self):
        return self._id_principal

    def modelo(self):
        return self.__modelo

    def mostrar_detalle(self):
        return f"Placa: {self._id_principal} | Modelo: {self.__modelo}"