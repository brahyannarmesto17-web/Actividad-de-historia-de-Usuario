from entidad.vehiculo import Vehiculo
from entidad.chofer import Chofer
from entidad.registro import RegistroControl, GestionRegistros # Importamos la nueva clase

# Creamos una única instancia del gestor
gestor = GestionRegistros()

def menu():
    while True:
        print(" --------- MENU DE CONTROL DE ACCESO ---------")
        print("1. Registrar nueva entrada")
        print("2. Ver todos los registros guardados")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("[ Digitacion de Datos ]")
            placa = input("Placa del vehículo: ")
            modelo = input("Modelo del vehículo: ")
            documento = input("Documento del chofer: ")
            nombre = input("Nombre del chofer: ")

            # Creamos el objeto registro
            registro = RegistroControl(Vehiculo(placa, modelo), Chofer(documento, nombre))

            # USAMOS EL GESTOR PARA GUARDAR
            gestor.guardar_registro(registro)
            print(" Registro guardado exitosamente.")

        elif opcion == "2":
            print("REPORTES DE DATOS GUARDADOS")
            print("-----------------------------------------------------------------------------------------")
            gestor.ver_reporte()
            print("-----------------------------------------------------------------------------------------")

        elif opcion == "3":
            print("Cerrando sistema...")
            break

if __name__ == "__main__":
    menu()