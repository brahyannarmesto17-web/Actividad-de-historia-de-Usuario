from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id_principal):
        self._id_principal = id_principal

    def mostrar_detalle(self):
        pass