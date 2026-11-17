"""
Clase Cliente.
Hereda de la clase abstracta Entidad.
"""

from clases.entidad import Entidad
from excepciones.excepciones import ClienteInvalidoError


class Cliente(Entidad):
    """Representa un cliente del sistema."""
    def __init__(self, id_entidad, nombre, correo, telefono):

        if not nombre or nombre.strip() == "":
            raise ClienteInvalidoError(
                "El nombre del cliente es obligatorio"
            )

        if not correo or correo.strip() == "":
            raise ClienteInvalidoError(
                "El correo del cliente es obligatorio"
            )

        if not telefono or telefono.strip() == "":
            raise ClienteInvalidoError(
                "El teléfono del cliente es obligatorio"
            )

        super().__init__(id_entidad, nombre)

        self.__correo = correo
        self.__telefono = telefono

    @property
    def correo(self):
        """Obtiene el correo del cliente."""
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        """Actualiza el correo del cliente."""

        if not nuevo_correo or nuevo_correo.strip() == "":
            raise ClienteInvalidoError(
                "El correo no puede estar vacío"
            )

        self.__correo = nuevo_correo

    @property
    def telefono(self):
        """Obtiene el teléfono del cliente."""
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        """Actualiza el teléfono del cliente."""

        if not nuevo_telefono or nuevo_telefono.strip() == "":
            raise ClienteInvalidoError(
                "El teléfono no puede estar vacío"
            )

        self.__telefono = nuevo_telefono

    def mostrar_info(self):
        """Muestra la información del cliente."""
        print(f"ID: {self.id_entidad}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")
        