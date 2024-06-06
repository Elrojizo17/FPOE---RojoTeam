import os
import tkinter as tk
from tkinter import PhotoImage
from Vistas.crear_cliente import CrearCliente
from Vistas.crear_servicio import CrearServicio
from Controladores.controladores import Controlador
from Controladores.ejecutar_backup import EjecutarBackup



class Vista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("465x300")
        self.ventana.geometry("+500+80")
        self.ventana.title("Menú Principal")
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()

        self.menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)

        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, 'logo.png')
        logo = PhotoImage(file=image_path)
        label_logo = tk.Label(self.ventana, image=logo)
        label_logo.pack()

        self.menuClientes = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Clientes", menu=self.menuClientes)
        self.menuClientes.add_command(label="Gestión de Clientes", command=self.registrarCliente)
        self.menuClientes.add_separator()

        self.menuServicios = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Servicios", menu=self.menuServicios)
        self.menuServicios.add_command(label="Gestión de Servicios", command=self.registrarServicio)

        self.menuSalir = tk.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=self.menuSalir)
        self.menuSalir.add_command(label="Salir", command=self.ventana.quit)

        self.ventana.after(0, self.iniciar_backup)
        self.ventana.mainloop()

    def iniciar_backup(self):
        url_clientes = "http://192.168.62.118:8000/v1/cliente"
        url_servicios = "http://192.168.62.118:8000/v1/servicio"

        backup = EjecutarBackup(url_clientes, url_servicios)
        backup.ejecutar_hilos()

    def registrarCliente(self):
        self.ventana.after(0, lambda: CrearCliente(self.ventana))

    def registrarServicio(self):
        self.ventana.after(0, lambda: CrearServicio(self.ventana))

if __name__ == "__main__":
    app = Vista()