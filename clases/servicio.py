"""
Clase abstracta Servicio y sus clases derivadas.
"""

from abc import ABC, abstractmethod
from excepciones.excepciones import ServicioInvalidoError
from logs.registro import logger


class Servicio(ABC):
    """Clase abstracta para los servicios del sistema."""

    def __init__(
        self,
        codigo,
        nombre,
        precio_base,
        disponible=True
    ):

        if not codigo or codigo.strip() == "":
            logger.error(
                "Intento de crear servicio sin código"
            )

            raise ServicioInvalidoError(
                "El código del servicio es obligatorio"
            )

        if not nombre or nombre.strip() == "":
            logger.error(
                "Intento de crear servicio sin nombre"
            )

            raise ServicioInvalidoError(
                "El nombre del servicio es obligatorio"
            )

        if precio_base <= 0:
            logger.error(
                "Intento de crear servicio con precio inválido"
            )

            raise ServicioInvalidoError(
                "El precio base debe ser mayor a cero"
            )

        self.codigo = codigo
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

        logger.info(
            "Servicio creado correctamente: %s",
            nombre
        )

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
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

        if capacidad <= 0:
            logger.error(
                "Intento de crear sala con capacidad inválida"
            )

            raise ServicioInvalidoError(
                "La capacidad debe ser mayor a cero"
            )

        self.capacidad = capacidad

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        costo = self.precio_base * duracion

        costo -= descuento
        costo += costo * impuesto

        return costo

    def mostrar_info(self):

        print("=== Reserva de Sala ===")
        print("Nombre:", self.nombre)
        print("Capacidad:", self.capacidad)


class AlquilerEquipo(Servicio):
    """Representa el servicio de alquiler de equipos."""

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

        if not tipo_equipo or tipo_equipo.strip() == "":
            logger.error(
                "Intento de crear equipo sin tipo"
            )

            raise ServicioInvalidoError(
                "Debe indicar un tipo de equipo"
            )

        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        costo = self.precio_base * duracion

        costo -= descuento
        costo += costo * impuesto

        return costo

    def mostrar_info(self):

        print("=== Alquiler de Equipo ===")
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo_equipo)


class AsesoriaEspecializada(Servicio):
    """Representa el servicio de asesorías especializadas."""

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

        if not especialidad or especialidad.strip() == "":
            logger.error(
                "Intento de crear asesoría sin especialidad"
            )

            raise ServicioInvalidoError(
                "Debe indicar una especialidad"
            )

        self.especialidad = especialidad

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        costo = self.precio_base * duracion

        costo -= descuento
        costo += costo * impuesto

        return costo

    def mostrar_info(self):

        print("=== Asesoría Especializada ===")
        print("Nombre:", self.nombre)
        print("Especialidad:", self.especialidad)
        