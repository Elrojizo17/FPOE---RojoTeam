import threading
import time
import logging
import requests

logging.basicConfig(level=logging.DEBUG)

class BackupClientes(threading.Thread):
    def __init__(self, nombrehc, url):
        threading.Thread.__init__(self, name=nombrehc)
        self.url ="http://localhost:8000/v1/cliente"

    def run(self):
        while True:
            self.consultarhc()
            time.sleep(45)
    
    def consultarhc(self):
        response=requests.get(self.url)
        data = response.json()
        with open("Clientes.txt", "w") as file:
            for cliente in data:
                file.write(str(cliente) + '\n')