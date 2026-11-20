"""
Simulaciones y casos de prueba del sistema.
"""

from clases.cliente import Cliente
from clases.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from clases.reserva import Reserva


def ejecutar_simulaciones():
    """Ejecuta las simulaciones del sistema."""

    clientes = []
    servicios = []
    reservas = []

    print("\n==============================")
    print("SIMULACION 1 - Cliente valido")
    print("==============================")

    try:
        cliente = Cliente(
            "C001",
            "Santiago",
            "santiago@gmail.com",
            "3001234567"
        )

        clientes.append(cliente)

        cliente.mostrar_info()

    except Exception as e:
        print("Error:", e)

    print("\n==============================")
    print("SIMULACION 2 - ReservaSala valida")
    print("==============================")

    try:
        sala = ReservaSala(
            "S001",
            "Sala Principal",
            50000,
            20
        )

        servicios.append(sala)

        sala.mostrar_info()

    except Exception as e:
        print("Error:", e)

    print("\n==============================")
    print("SIMULACION 3 - AlquilerEquipo valido")
    print("==============================")

    try:
        equipo = AlquilerEquipo(
            "E001",
            "Portatil Gamer",
            30000,
            "Laptop"
        )

        servicios.append(equipo)

        equipo.mostrar_info()

    except Exception as e:
        print("Error:", e)

    print("\n==============================")
    print("SIMULACION 4 - Asesoria valida")
    print("==============================")

    try:
        asesoria = AsesoriaEspecializada(
            "A001",
            "Asesoria Python",
            70000,
            "Programacion"
        )

        servicios.append(asesoria)

        asesoria.mostrar_info()

    except Exception as e:
        print("Error:", e)

    print("\n==============================")
    print("SIMULACION 5 - Reserva exitosa")
    print("==============================")

    try:
        cliente = Cliente(
            "C002",
            "Maria",
            "maria@gmail.com",
            "3011111111"
        )

        sala = ReservaSala(
            "S002",
            "Sala Ejecutiva",
            50000,
            10
        )

        reserva = Reserva(
            "R001",
            cliente,
            sala,
            2
        )

        reservas.append(reserva)

        reserva.procesar()

    except Exception as e:
        print("Error:", e)

    print("\n==============================")
    print("SIMULACION 6 - Cliente sin nombre")
    print("==============================")

    try:
        Cliente(
            "C003",
            "",
            "correo@gmail.com",
            "3000000000"
        )

    except Exception as e:
        print("Error controlado:", e)

    print("\n==============================")
    print("SIMULACION 7 - Cliente sin correo")
    print("==============================")

    try:
        Cliente(
            "C004",
            "Pedro",
            "",
            "3000000000"
        )

    except Exception as e:
        print("Error controlado:", e)

    print("\n==============================")
    print("SIMULACION 8 - Servicio con precio negativo")
    print("==============================")

    try:
        ReservaSala(
            "S003",
            "Sala Error",
            -50000,
            10
        )

    except Exception as e:
        print("Error controlado:", e)

    print("\n==============================")
    print("SIMULACION 9 - Reserva sin cliente")
    print("==============================")

    try:
        sala = ReservaSala(
            "S004",
            "Sala Norte",
            40000,
            5
        )

        Reserva(
            "R002",
            None,
            sala,
            1
        )

    except Exception as e:
        print("Error controlado:", e)

    print("\n==============================")
    print("SIMULACION 10 - Reserva con duración negativa")
    print("==============================")

    try:
        cliente = Cliente(
            "C005",
            "Ana",
            "ana@gmail.com",
            "3022222222"
        )

        sala = ReservaSala(
            "S005",
            "Sala Sur",
            50000,
            8
        )

        Reserva(
            "R003",
            cliente,
            sala,
            -2
        )

    except Exception as e:
        print("Error controlado:", e)

    print("\n==============================")
    print("SIMULACION 11 - Servicio no disponible")
    print("==============================")

    try:

        cliente = Cliente(
            "C006",
            "Luis",
            "luis@gmail.com",
            "3009999999"
        )

        sala = ReservaSala(
            "S006",
            "Sala Bloqueada",
            50000,
            10,
            disponible=False
        )

        reserva = Reserva(
            "R004",
            cliente,
            sala,
            2
        )

        reserva.procesar()

    except Exception as e:
        print("Error controlado:", e)

        if e.__cause__:
            print("Causa:", e.__cause__)

    print("\n==============================")
    print("SIMULACION 12 - Doble cancelacion")
    print("==============================")

    try:

        cliente = Cliente(
            "C007",
            "Laura",
            "laura@gmail.com",
            "3015555555"
        )

        sala = ReservaSala(
            "S007",
            "Sala Oeste",
            30000,
            5
        )

        reserva = Reserva(
            "R005",
            cliente,
            sala,
            1
        )

        reserva.cancelar()
        reserva.cancelar()

    except Exception as e:
        print("Error controlado:", e)

    print("\n==============================")
    print("SIMULACION 13 - Alquiler de equipo con descuento")
    print("==============================")

    try:

        equipo = AlquilerEquipo(
            "E002",
            "Portatil Empresarial",
            30000,
            "Laptop"
        )

        print(
            "Costo:",
            equipo.calcular_costo(
                2,
                descuento=5000,
                impuesto=0.19
            )
        )

    except Exception as e:
        print("Error:", e)

    print("\n==============================")
    print("SIMULACION 14 - Asesoria especializada con impuesto")
    print("==============================")

    try:

        asesoria = AsesoriaEspecializada(
            "A002",
            "Asesoria IA",
            80000,
            "Inteligencia Artificial"
        )

        print(
            "Costo:",
            asesoria.calcular_costo(
                3,
                descuento=10000,
                impuesto=0.19
            )
        )

    except Exception as e:
        print("Error:", e)

    print("\n==============================")
    print("RESUMEN DEL SISTEMA")
    print("==============================")

    print("Clientes registrados:", len(clientes))
    print("Servicios registrados:", len(servicios))
    print("Reservas registradas:", len(reservas))


if __name__ == "__main__":
    ejecutar_simulaciones()