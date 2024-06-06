import threading
import datetime
import logging
from .backup_clientes import BackupClientes
from .backup_servicios import BackupServicios

logging.basicConfig(level=logging.DEBUG)

class EjecutarBackup:
    def __init__(self, urlc, urls):
        self.urlc = urlc
        self.urls = urls

    def ejecutar_hilos(self):
        tiempo_de_inicio = datetime.datetime.now()

        backup_clientes = BackupClientes('backup_clientes', self.urlc)
        backup_servicios = BackupServicios('backup_servicios', self.urls)

        backup_clientes.start()
        backup_servicios.start()

        tiempo_final=datetime.datetime.now()
        logging.debug('Tiempo de ejecución: ' + str((tiempo_final - tiempo_de_inicio).total_seconds()) + ' segundos\n')
