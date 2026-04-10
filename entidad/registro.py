from datetime import datetime

# Tu clase de entidad (la que ya tenías)
class RegistroControl:
    def __init__(self, vehiculo, chofer):
        self.__obj_vehiculo = vehiculo
        self.__obj_chofer = chofer
        self.__hora = datetime.now().strftime("%H:%M:%S")

    def imprimir_registro(self):
        return f"Hora: {self.__hora} | {self.__obj_vehiculo.mostrar_detalle()} | {self.__obj_chofer.mostrar_detalle()}"

class GestionRegistros:
    def __init__(self):
        self.base_datos = []

    def guardar_registro(self, registro):
        self.base_datos.append(registro)

    def ver_reporte(self):
        if not self.base_datos:
            print("No hay registros para mostrar.")
        else:
            for registro in self.base_datos:
                print(registro.imprimir_registro())