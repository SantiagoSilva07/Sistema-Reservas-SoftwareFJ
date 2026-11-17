"""
Excepciones personalizadas del sistema.
Fase 4 - Sistema Integral de Gestión de Clientes,
Servicios y Reservas Software FJ.
"""

# ==========================
# EXCEPCIONES DE CLIENTE
# ==========================

class ClienteError(Exception):
    """Clase base para errores de cliente."""


class ClienteInvalidoError(ClienteError):
    """Datos inválidos del cliente."""


# ==========================
# EXCEPCIONES DE SERVICIO
# ==========================

class ServicioError(Exception):
    """Clase base para errores de servicio."""


class ServicioNoDisponibleError(ServicioError):
    """Servicio no disponible para reserva."""


class ServicioInvalidoError(ServicioError):
    """Datos inválidos del servicio."""


# ==========================
# EXCEPCIONES DE RESERVA
# ==========================

class ReservaError(Exception):
    """Clase base para errores de reserva."""


class ReservaIncorrectaError(ReservaError):
    """Error durante la creación o procesamiento."""


class OperacionNoPermitidaError(ReservaError):
    """Operación no permitida para la reserva."""
    