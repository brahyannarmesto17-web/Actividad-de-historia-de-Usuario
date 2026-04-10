from .base_datos import Entidad

class Chofer(Entidad):
    def __init__(self, documento, nombre):
        super().__init__(documento)
        self.__nombre = nombre

    def documento(self):
        return self._id_principal

    def nombre(self):
        return self.__nombre

    def mostrar_detalle(self):
        return f"Chofer: {self.__nombre} | ID: {self._id_principal}"