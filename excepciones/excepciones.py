"""
Excepciones personalizadas del sistema.
Fase 4 - Sistema Integral de Gestión de Clientes,
Servicios y Reservas Software FJ.
"""

# ==========================
# CLASE BASE DEL SISTEMA
# ==========================

class SistemaError(Exception):
    """Clase base para todas las excepciones del sistema."""


# ==========================
# EXCEPCIONES DE CLIENTE
# ==========================

class ClienteError(SistemaError):
    """Clase base para errores de cliente."""


class ClienteInvalidoError(ClienteError):
    """Datos inválidos del cliente."""


# ==========================
# EXCEPCIONES DE SERVICIO
# ==========================

class ServicioError(SistemaError):
    """Clase base para errores de servicio."""


class ServicioNoDisponibleError(ServicioError):
    """Servicio no disponible para reserva."""


class ServicioInvalidoError(ServicioError):
    """Datos inválidos del servicio."""


# ==========================
# EXCEPCIONES DE RESERVA
# ==========================

class ReservaError(SistemaError):
    """Clase base para errores de reserva."""


class ReservaIncorrectaError(ReservaError):
    """Error durante la creación o procesamiento."""


class OperacionNoPermitidaError(ReservaError):
    """Operación no permitida para la reserva."""
    