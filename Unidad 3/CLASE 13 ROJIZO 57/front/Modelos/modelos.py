import tkinter as tk

class Modelos:
    def __init__(self, marca, cilindraje,modelo,color):
        self.marca = tk.StringVar(value=marca)
        self.cilindraje = tk.IntVar(value=cilindraje)
        self.modelo = tk.IntVar(value=modelo)
        self.color = tk.StringVar(value=color)
        self.id = tk.StringVar(value=id)

    