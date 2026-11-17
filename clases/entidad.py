"""
Clase abstracta general del sistema.
"""

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase base abstracta para las entidades del sistema.
    """

    def __init__(self, id_entidad, nombre):
        self.id_entidad = id_entidad
        self.nombre = nombre

    @abstractmethod
    def mostrar_info(self):
        """
        Metodo abstracto que deberan implementar las clases hijas.
        """
        