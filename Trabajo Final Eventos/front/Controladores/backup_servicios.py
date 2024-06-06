import threading
import time
import logging
import requests

logging.basicConfig(level=logging.DEBUG)

class BackupServicios(threading.Thread):
    def __init__(self, nombrehs, url):
        threading.Thread.__init__(self, name=nombrehs)
        self.url ="http://localhost:8000/v1/servicio"

    def run(self):
        while True:
            self.consultarhs()
            time.sleep(45)
    
    def consultarhs(self):
        response=requests.get(self.url)
        data = response.json()
        with open("Servicios.txt", "w") as file:
            for servicio in data:
                file.write(str(servicio) + '\n')