import threading
import logging
import time

class Hilo6(threading.Thread):
    def __init__(self, nombre_hilo, condicion, lock_escritura, bandera_ejecucion):
        threading.Thread.__init__(self, name=nombre_hilo)
        self.condicion = condicion
        self.lock_escritura = lock_escritura
        self.bandera_ejecucion = bandera_ejecucion

    def run(self):
        while True:
            nombre = input("Por favor, introduce tu nombre: ")
            with self.lock_escritura:
                print("Nombre introducido:", nombre)
                self.guardar_nombre(nombre)
                self.condicion.notify()  # Notificar al hilo 5 que se ha introducido un nombre
                self.bandera_ejecucion.set()  # Establecer la bandera en True para permitir la ejecución de Hilo5
            
            time.sleep(5)  # Esperar 5 segundos antes de solicitar el próximo nombre
            self.bandera_ejecucion.clear()  # Reiniciar la bandera de ejecución después de 5 segundos

    def guardar_nombre(self, nombre):
        with open("nombres.txt", "a") as file:
            file.write(nombre + "\n")
            logging.debug(f"Nombre guardado en archivo: {nombre}")
