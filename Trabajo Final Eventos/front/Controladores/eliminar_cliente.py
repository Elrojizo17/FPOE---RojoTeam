import tkinter.messagebox as messagebox
import requests
from Modelos.cliente import Cliente

class EliminarClientes:
    def __init__(self, vista):
        self.vista = vista
        self.cliente = Cliente("", "", "", "", "")

