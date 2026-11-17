ARQUITECTURA DEL SISTEMA

CLASE ABSTRACTA GENERAL

Entidad
- id
- nombre
- mostrar_info()

CLASE CLIENTE

Hereda de Entidad

Atributos:
- id
- nombre
- correo
- telefono

Validaciones:
- nombre obligatorio
- correo obligatorio
- telefono obligatorio

CLASE ABSTRACTA SERVICIO

Atributos:
- codigo
- nombre
- precio_base
- disponible

Metodos:
- calcular_costo()
- mostrar_info()

SERVICIOS DERIVADOS

ReservaSala
- capacidad

AlquilerEquipo
- tipo_equipo

AsesoriaEspecializada
- especialidad

CLASE RESERVA

Atributos:
- id_reserva
- cliente
- servicio
- duracion
- estado

Metodos:
- confirmar()
- cancelar()
- procesar()
- mostrar_info()

EXCEPCIONES

- ClienteError
- ClienteInvalidoError
- ServicioError
- ServicioNoDisponibleError
- ServicioInvalidoError
- ReservaError
- ReservaIncorrectaError
- OperacionNoPermitidaError

LOGS

- sistema.log

SIMULACIONES

- minimo 10 casos
- validos
- invalidos
- sistema debe continuar funcionando