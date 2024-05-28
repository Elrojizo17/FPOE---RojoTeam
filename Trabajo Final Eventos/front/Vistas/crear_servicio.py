import tkinter as tk
import tkinter.messagebox as messagebox
from Controladores.registrar_servicio import Registrar_servicio

class CrearServicio():
    def __init__(self, menu):
        self.ventana = tk.Toplevel(menu)
        self.ventana.focus_set()
        self.ventana.title("Registrar Servicio")
        self.ventana.geometry("1000x1000")
        self.ventana.resizable(0, 0)
        self.controladores = Registrar_servicio(self)

        self.nombre_servicio= tk.StringVar()
        self.cedula_cliente=tk.StringVar()
        self.descripcion=tk.StringVar()
        self.valor=tk.StringVar()

        self.crear_interfaz_servicio()

    def crear_interfaz_servicio(self):
        self.titulo = tk.Label(self.ventana, text="Registrar Servicio")
        self.titulo.grid(row=0, column=0, columnspan=2)

        self.lblNombreServicio = tk.Label(self.ventana, text="Nombre del Servicio: ")
        self.lblNombreServicio.grid(row=1, column=0)
        self.txtNombreServicio = tk.Entry(self.ventana)
        self.txtNombreServicio.grid(row=1, column=1)
        self.txtNombreServicio.bind("<KeyRelease>", lambda event: self.controladores.val_nombre_servicio(event, self.txtNombreServicio))
        self.lblNombreServicioAdvertencia = tk.Label(self.ventana, text="", fg="red")
        #self.lblNombreServicioAdvertencia.grid(row=2, column=0, columnspan=2)

        self.lblCedulaCServicio = tk.Label(self.ventana, text="Cedula del Cliente: ")
        self.lblCedulaCServicio.grid(row=2, column=0)
        self.txtCedulaServicio = tk.Entry(self.ventana)
        self.txtCedulaServicio.grid(row=2, column=1)
        self.txtCedulaServicio.bind("<KeyRelease>", lambda event: self.controladores.val_cedula_servicio(event, self.txtCedulaServicio))
        self.lblCedulaServicioAdvertencia = tk.Label(self.ventana, text="", fg="red")
        #self.lblCedulaServicioAdvertencia.grid(row=4, column=0, columnspan=2)

        self.lblDescripcion = tk.Label(self.ventana, text="Descripción: ")
        self.lblDescripcion.grid(row=3, column=0)
        self.txtDescripcion = tk.Entry(self.ventana)
        self.txtDescripcion.grid(row=3, column=1)
        self.txtDescripcion.bind("<KeyRelease>", lambda event: self.controladores.val_descripcion(event, self.txtDescripcion))
        self.lblDescripcionAdvertencia = tk.Label(self.ventana, text="", fg="red")
        #self.lblDescripcionAdvertencia.grid(row=6, column=0, columnspan=2)

        self.lblValor = tk.Label(self.ventana, text="Valor: ")
        self.lblValor.grid(row=4, column=0)
        self.txtValor = tk.Entry(self.ventana)
        self.txtValor.grid(row=4, column=1)
        self.txtValor.bind("<KeyRelease>", lambda event: self.controladores.val_valor(event, self.txtValor))
        self.lblValorAdvertencia = tk.Label(self.ventana, text="", fg="red")
        #self.lblValorAdvertencia.grid(row=8, column=0, columnspan=2)

        self.btnGuardar = tk.Button(self.ventana, text="Guardar", command=self.controladores.validar_Servicio)
        self.btnGuardar.grid(row=5, column=0, columnspan=2)

        self.btnConsultar_todo= tk.Button(self.ventana, text="Consultar todo",command=lambda:self.controladores.boton_consultar_servicio_todo())
        self.btnConsultar_todo.grid(row=6, column=0, padx=15, pady=15)

        self.btnConsultar_CC=tk.Button(self.ventana, text="Consultar Cédula del Cliente",command=lambda:self.controladores.boton_consultar_servicio_todo())
        self.btnConsultar_CC.grid(row=7, column=1, padx=15, pady=15)
