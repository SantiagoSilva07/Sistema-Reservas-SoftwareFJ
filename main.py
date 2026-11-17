"""
Archivo principal de pruebas e integración del sistema.
"""
from clases.cliente import Cliente
from clases.servicio import ReservaSala
from clases.reserva import Reserva


try:
    # Crear cliente
    cliente = Cliente(
        "C001",
        "Santiago David Silva",
        "santiago@gmail.com",
        "3001234567"
    )

    # Crear servicio
    servicio = ReservaSala(
        "S001",
        "Sala Principal",
        50000,
        20
    )

    # Crear reserva
    reserva = Reserva(
        "R001",
        cliente,
        servicio,
        2
    )

    print("===== CLIENTE =====")
    cliente.mostrar_info()

    print("\n===== SERVICIO =====")
    servicio.mostrar_info()

    print("\n===== RESERVA =====")
    reserva.procesar()
    reserva.mostrar_info()

except Exception as e:
    print("ERROR:", e)
    