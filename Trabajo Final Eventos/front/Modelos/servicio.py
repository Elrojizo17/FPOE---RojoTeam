import tkinter as tk

class Servicio():
    def __init__(self, nombre_servicio, cedula_cliente, descripcion, valor):
        self.nombre_servicio = tk.StringVar(value=nombre_servicio)
        self.cedula = tk.StringVar(value=cedula_cliente)
        self.descripcion = tk.StringVar(value=descripcion)
        self.valor = tk.IntVar(value=valor)
