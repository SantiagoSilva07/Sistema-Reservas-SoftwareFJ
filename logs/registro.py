"""
Modulo centralizado para el registro de eventos y errores.
"""

import logging
import os

# Crear carpeta logs si no existe
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configuracion del archivo de registro
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Logger del sistema
logger = logging.getLogger("SoftwareFJ")
