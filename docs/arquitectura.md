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

Características:
- encapsulación mediante propiedades
- manejo de excepciones personalizadas
- registro de errores y eventos en logs

CLASE ABSTRACTA SERVICIO

Atributos:
- codigo
- nombre
- precio_base
- disponible

Métodos:
- calcular_costo(duracion, descuento=0, impuesto=0)
- mostrar_info()

Validaciones:
- codigo obligatorio
- nombre obligatorio
- precio_base mayor a cero

SERVICIOS DERIVADOS

ReservaSala
- capacidad

Validaciones:
- capacidad mayor a cero

AlquilerEquipo
- tipo_equipo

Validaciones:
- tipo_equipo obligatorio

AsesoriaEspecializada
- especialidad

Validaciones:
- especialidad obligatoria

CLASE RESERVA

Atributos:
- id_reserva
- cliente
- servicio
- duracion
- estado

Métodos:
- confirmar()
- cancelar()
- procesar()
- mostrar_info()

Validaciones:
- cliente obligatorio
- servicio obligatorio
- duración mayor a cero

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

Archivo:
- sistema.log

Registra:
- creación de clientes
- creación de servicios
- creación de reservas
- errores de clientes
- errores de servicios
- errores de reservas
- eventos relevantes del sistema

GESTIÓN DE DATOS

Listas utilizadas:
- clientes
- servicios
- reservas

Operaciones:
- almacenamiento en memoria
- gestión mediante objetos y listas
- sin uso de bases de datos

SIMULACIONES

Casos implementados:
- cliente válido
- reserva de sala válida
- alquiler de equipo válido
- asesoría especializada válida
- reserva exitosa
- cliente sin nombre
- cliente sin correo
- servicio con precio inválido
- reserva sin cliente
- reserva con duración inválida
- servicio no disponible
- doble cancelación
- cálculo con descuento
- cálculo con impuesto

Características:
- manejo de excepciones personalizadas
- uso de try / except
- uso de try / except / else / finally
- encadenamiento de excepciones (__cause__)
- registro de eventos y errores en logs
- continuidad del sistema ante errores