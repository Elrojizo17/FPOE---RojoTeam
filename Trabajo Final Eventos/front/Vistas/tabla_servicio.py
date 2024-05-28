import tkinter as tk
from tkinter import ttk

class TablaServicio():
    def __init__(self, vistas, titulos, columnas, data):
        self.tabla_S=ttk.Treeview(vistas, columns=columnas, show="headings")
        for posicion in range(0,len(columnas)):
            self.tabla_S.heading(columnas[posicion], text=titulos[posicion])
        for elemento in data:
            self.tabla_S.insert(parent='',index=0, values=elemento)

    def refrescar_tablaS(self, data):
        self.tabla_S.delete(*self.tabla_S.get_children())
        for elemento in data:
            self.tabla_S.insert(parent='',index=0, values=elemento)