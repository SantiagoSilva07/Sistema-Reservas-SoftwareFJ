"""
Clase abstracta Servicio y sus clases derivadas.
"""

from abc import ABC, abstractmethod


class Servicio(ABC):
    """Clase abstracta para los servicios del sistema."""

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        disponible=True
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, descuento=0, impuesto=0):
        """Calcula el costo del servicio."""

    @abstractmethod
    def mostrar_info(self):
        """Muestra la información del servicio."""


class ReservaSala(Servicio):
    """Representa el servicio de reserva de salas."""
    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        capacidad,
        disponible=True
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base,
            disponible
        )
        self.capacidad = capacidad

    def calcular_costo(self, descuento=0, impuesto=0):

        costo = self.precio_base

        costo -= descuento
        costo += costo * impuesto

        return costo

    def mostrar_info(self):

        print("=== Reserva de Sala ===")
        print("Nombre:", self.nombre)
        print("Capacidad:", self.capacidad)


class AlquilerEquipo(Servicio):
    """Representa el servicio de reserva de salas."""

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        tipo_equipo,
        disponible=True
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base,
            disponible
        )
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, descuento=0, impuesto=0):

        costo = self.precio_base

        costo -= descuento
        costo += costo * impuesto

        return costo

    def mostrar_info(self):

        print("=== Alquiler de Equipo ===")
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo_equipo)


class AsesoriaEspecializada(Servicio):
    """Representa el servicio de reserva de salas."""

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        especialidad,
        disponible=True
    ):
        super().__init__(
            codigo,
            nombre,
            precio_base,
            disponible
        )
        self.especialidad = especialidad

    def calcular_costo(self, descuento=0, impuesto=0):

        costo = self.precio_base

        costo -= descuento
        costo += costo * impuesto

        return costo

    def mostrar_info(self):

        print("=== Asesoría Especializada ===")
        print("Nombre:", self.nombre)
        print("Especialidad:", self.especialidad)
        