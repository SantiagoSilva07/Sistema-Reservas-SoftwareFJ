# Tema 3: Gestion de Reservas
# Autor: Luis Carlos Ortega Moreno
# Usuario GitHub: luisk0411-design
# Rama: feature/gestion-reservas
# Fase 4 - Programacion 213023

# Estas excepciones son las que vamos a usar en reservas.
# Las puse aqui para poder probar mi parte mientras Santiago
# termina el archivo de excepciones del grupo.

class ReservaIncorrectaError(Exception):
    pass

class ServicioNoDisponibleError(Exception):
    pass

class OperacionNoPermitidaError(Exception):
    pass


class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion):
        # Validar que no falte el id
        if id_reserva == "" or id_reserva is None:
            raise ValueError("El id de la reserva es obligatorio")

        # Validar que si vengan cliente y servicio
        if cliente is None:
            raise ValueError("La reserva necesita un cliente")
        if servicio is None:
            raise ValueError("La reserva necesita un servicio")

        # Validar la duracion
        if duracion <= 0:
            raise ReservaIncorrectaError("La duracion debe ser mayor a 0")

        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def confirmar(self):
        # Si el servicio no esta disponible no se puede confirmar
        if self.servicio.disponible == False:
            raise ServicioNoDisponibleError("El servicio no esta disponible")

        if self.estado == "confirmada":
            raise OperacionNoPermitidaError("La reserva ya esta confirmada")

        if self.estado == "cancelada":
            raise OperacionNoPermitidaError("No se puede confirmar una reserva cancelada")

        self.estado = "confirmada"
        print("Reserva confirmada:", self.id_reserva)

    def cancelar(self):
        if self.estado == "cancelada":
            raise OperacionNoPermitidaError("La reserva ya esta cancelada")

        self.estado = "cancelada"
        print("Reserva cancelada:", self.id_reserva)

    def procesar(self):
        # Aqui uso try, except, else y finally como pide la guia
        try:
            self.confirmar()
            costo = self.servicio.calcular_costo()
        except Exception as e:
            # Encadenamiento, guardo el error original
            raise ReservaIncorrectaError("No se pudo procesar la reserva") from e
        else:
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
