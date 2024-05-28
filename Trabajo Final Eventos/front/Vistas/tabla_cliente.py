import tkinter as tk
from tkinter import ttk

class TablaCliente():
    def __init__(self, vistas, titulos, columnas, data):
        self.tabla_C=ttk.Treeview(vistas, columns=columnas, show="headings")
        for posicion in range(0,len(columnas)):
            self.tabla_C.heading(columnas[posicion], text=titulos[posicion])
        for elemento in data:
            self.tabla_C.insert(parent='',index=0, values=elemento)

    def refrescar_tablaC(self, data):
        self.tabla_C.delete(*self.tabla_C.get_children())
        for elemento in data:
            self.tabla_C.insert(parent='',index=0, values=elemento)