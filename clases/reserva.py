
# Tema 3: Gestion de Reservas
# Autor: Luis Carlos Ortega Moreno
# Usuario GitHub: luisk0411-design
# Rama: feature/gestion-reservas
# Fase 4 - Programacion 213023

# Correccion final segun observacion del tutor Alexander 14 nov:
# Ya no queda ningun error generico, todo es con excepciones propias
# Y ya queda el registro en logs/reservas.log

import logging
import os

# Estas excepciones son las que vamos a usar en reservas.
# Las puse aqui para poder probar mi parte mientras Santiago
# termina el archivo de excepciones del grupo.

class ReservaIncorrectaError(Exception):
    pass

class ServicioNoDisponibleError(Exception):
    pass

class OperacionNoPermitidaError(Exception):
    pass


# Configuracion sencilla del log, para que quede registro en logs/reservas.log
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/reservas.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion):
        # Validar que no falte el id
        # Ahora es ReservaIncorrectaError como pidio el tutor
        if id_reserva == "" or id_reserva is None:
            logging.error("Intento de crear reserva sin id")
            raise ReservaIncorrectaError("El id de la reserva es obligatorio")

        # Validar que si vengan cliente y servicio
        # Ahora son ReservaIncorrectaError
        if cliente is None:
            logging.error("Intento de crear reserva sin cliente")
            raise ReservaIncorrectaError("La reserva necesita un cliente")
        if servicio is None:
            logging.error("Intento de crear reserva sin servicio")
            raise ReservaIncorrectaError("La reserva necesita un servicio")

        # Validar la duracion, debe ser un numero y mayor a 0
        if type(duracion) != int and type(duracion) != float:
            logging.error("Duracion con tipo incorrecto: %s", duracion)
            raise ReservaIncorrectaError("La duracion debe ser un numero")
        if duracion <= 0:
            logging.error("Duracion menor o igual a 0: %s", duracion)
            raise ReservaIncorrectaError("La duracion debe ser mayor a 0")

        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
        logging.info("Reserva creada: %s", self.id_reserva)

    def confirmar(self):
        # Si el servicio no esta disponible no se puede confirmar
        if self.servicio.disponible == False:
            logging.error("Reserva %s no se pudo confirmar, servicio no disponible", self.id_reserva)
            raise ServicioNoDisponibleError("El servicio no esta disponible")

        if self.estado == "confirmada":
            logging.error("Reserva %s ya estaba confirmada", self.id_reserva)
            raise OperacionNoPermitidaError("La reserva ya esta confirmada")

        if self.estado == "cancelada":
            logging.error("Reserva %s cancelada, no se puede confirmar", self.id_reserva)
            raise OperacionNoPermitidaError("No se puede confirmar una reserva cancelada")

        self.estado = "confirmada"
        logging.info("Reserva confirmada: %s", self.id_reserva)
        print("Reserva confirmada:", self.id_reserva)

    def cancelar(self):
        if self.estado == "cancelada":
            logging.error("Reserva %s ya estaba cancelada", self.id_reserva)
            raise OperacionNoPermitidaError("La reserva ya esta cancelada")

        self.estado = "cancelada"
        logging.info("Reserva cancelada: %s", self.id_reserva)
        print("Reserva cancelada:", self.id_reserva)

    def procesar(self):
        # Aqui uso try, except, else y finally como pide la guia
        try:
            self.confirmar()
            costo = self.servicio.calcular_costo()
        except Exception as e:
            # Registro dentro del except, este es el manejo definitivo del error
            logging.error("No se pudo procesar la reserva %s, error: %s", self.id_reserva, e)
            # Encadenamiento, guardo el error original
            raise ReservaIncorrectaError("No se pudo procesar la reserva") from e
        else:
            logging.info("Reserva procesada: %s, costo: %s", self.id_reserva, costo)
            print("Reserva procesada, costo:", costo)
            return costo
        finally:
            print("Se termino de intentar procesar la reserva", self.id_reserva)

    def mostrar_info(self):
        print("Reserva:", self.id_reserva)
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Duracion:", self.duracion)
        print("Estado:", self.estado)


# Prueba rapida para ver si funciona mi parte
if __name__ == "__main__":
    # Clases de prueba para no depender de los otros temas todavia
    class ClientePrueba:
        def __init__(self, nombre):
            self.nombre = nombre

    class ServicioPrueba:
        def __init__(self, nombre, disponible=True):
            self.nombre = nombre
            self.disponible = disponible

        def calcular_costo(self):
            return 50000

    print("=== Prueba 1: reserva buena ===")
    try:
        cliente1 = ClientePrueba("Luis Carlos Ortega")
        servicio1 = ServicioPrueba("Sala A")
        reserva1 = Reserva("R01", cliente1, servicio1, 2)
        reserva1.procesar()
        reserva1.mostrar_info()
    except Exception as e:
        print("Error:", e)

    print("\n=== Prueba 2: duracion mala ===")
    try:
        cliente2 = ClientePrueba("Ana")
        servicio2 = ServicioPrueba("Sala B")
        reserva2 = Reserva("R02", cliente2, servicio2, 0)
    except Exception as e:
        print("Error controlado:", e)

    print("\n=== Prueba 3: servicio no disponible ===")
    try:
        cliente3 = ClientePrueba("Juan")
        servicio3 = ServicioPrueba("Sala C", False)
        reserva3 = Reserva("R03", cliente3, servicio3, 1)
        reserva3.procesar()
    except Exception as e:
        print("Error controlado:", e)
        print("Causa:", e.__cause__)

    print("\n=== Prueba 4: cancelar dos veces ===")
    try:
        reserva1.cancelar()
        reserva1.cancelar()
    except Exception as e:
        print("Error controlado:", e)

    print("\n=== Prueba 5: duracion con texto ===")
    try:
        cliente5 = ClientePrueba("Maria")
        servicio5 = ServicioPrueba("Sala D")
        reserva5 = Reserva("R05", cliente5, servicio5, "dos")
    except Exception as e:
        print("Error controlado:", e)

    print("\n=== Prueba 6: reserva sin id ===")
    try:
        cliente6 = ClientePrueba("Pedro")
        servicio6 = ServicioPrueba("Sala E")
        reserva6 = Reserva("", cliente6, servicio6, 1)
    except Exception as e:
        print("Error controlado:", e)
        print("Tipo de error:", type(e).__name__)

    print("\n=== Prueba 7: reserva sin cliente ===")
    try:
        servicio7 = ServicioPrueba("Sala F")
        reserva7 = Reserva("R07", None, servicio7, 1)
    except Exception as e:
        print("Error controlado:", e)
        print("Tipo de error:", type(e).__name__)

    print("\nRevisa el archivo logs/reservas.log, ahi deben quedar guardados los eventos y errores")

