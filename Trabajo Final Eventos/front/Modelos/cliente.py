import tkinter as tk

class Clientes:
    def __init__(self, nombre, apellido, cedula, telefono, correo):
        self.nombre = tk.StringVar(value=nombre)
        self.apellido = tk.StringVar(value=apellido)
        self.cedula = tk.StringVar(value=cedula)
        self.telefono = tk.StringVar(value=telefono)
        self.correo = tk.StringVar(value=correo)

