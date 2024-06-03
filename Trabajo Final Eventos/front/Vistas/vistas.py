import os
import tkinter
from tkinter import PhotoImage
from Vistas.crear_cliente import CrearCliente
from Vistas.crear_servicio import CrearServicio
from Controladores.controladores import Controlador

class Vista():
    def __init__(self):
        self.ventana = tkinter.Tk()        
        self.ventana.geometry("465x300")
        self.ventana.geometry("+500+80")
        self.ventana.title("Menú Principal")
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()
        
        self.controladores = Controlador(self)

        self.menu = tkinter.Menu(self.ventana)
        self.ventana.config(menu=self.menu)
        
        # Obtener la ruta del directorio actual del script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Concatenar el nombre de la imagen al final de la ruta del directorio
        image_path = os.path.join(script_dir, 'logo.png')

        logo = PhotoImage(file=image_path)

        # Agregar el logo como un Label en la parte superior
        label_logo = tkinter.Label(self.ventana, image=logo)
        label_logo.pack()

        self.menuClientes = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Clientes", menu=self.menuClientes)
        self.menuClientes.add_command(label="Gestión de Clientes", command=lambda: self.registrarCliente())
        self.menuClientes.add_separator()
        

        self.menuServicios = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Servicios", menu=self.menuServicios)
        self.menuServicios.add_command(label="Gestión de Servicios", command=lambda: self.registrarServicio())

        self.menuSalir = tkinter.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=self.menuSalir)
        self.menuSalir.add_command(label="Salir", command=lambda: self.controladores.el_usuario_quiere_salir())

        self.ventana.mainloop()

    def registrarCliente(self):
        interfaz_cliente = CrearCliente(self.menu)

    def registrarServicio(self):
        interfaz_servicio = CrearServicio(self.menu)
