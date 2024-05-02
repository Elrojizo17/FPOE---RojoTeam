import threading
import logging
import time

class Hilo5(threading.Thread):
    def __init__(self, nombre_hilo, condicion, bandera_ejecucion):
        threading.Thread.__init__(self, name=nombre_hilo)
        self.condicion = condicion
        self.bandera_ejecucion = bandera_ejecucion

    def run(self):
        while True:
            with self.condicion:
                self.condicion.wait()  # Esperar la señal para comenzar la ejecución
                try:
                    while True:  # Ejecutar infinitamente
                        logging.debug('Esto se escribe infinitamente')
                        time.sleep(1)  # Esperar 1 segundo para evitar el bloqueo de la CPU
                        if not self.bandera_ejecucion.is_set():  # Verificar si la bandera ha sido desactivada
                            break  # Salir del bucle si la bandera ha sido desactivada
                except KeyboardInterrupt:
                    logging.debug('Hilo 5 interrumpido manualmente')
                    break
                finally:
                    self.bandera_ejecucion.clear()  # Restablecer la bandera de ejecución después de 5 segundos
