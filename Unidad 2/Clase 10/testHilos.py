import threading
import logging
from hilo5 import Hilo5
from hilo6 import Hilo6

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

lock_escritura = threading.Lock()
nombre_introducido_condicion = threading.Condition(lock_escritura)
bandera_ejecucion = threading.Event()  # Bandera para controlar la ejecución de Hilo5

condicion = nombre_introducido_condicion  # Compartir la misma condición entre los hilos

hilo_5 = Hilo5('hilo_5', condicion, bandera_ejecucion)
hilo_6 = Hilo6('hilo_6', condicion, lock_escritura, bandera_ejecucion)

# Iniciar los hilos
# Iniciar los hilos
hilo_5.start()
hilo_6.start()

# Establecer la bandera de ejecución en True para que el hilo 5 comience a ejecutarse
bandera_ejecucion.set()

# Esperar a que los hilos terminen (esto no ocurrirá ya que son bucles infinitos)
hilo_5.join()
hilo_6.join()

