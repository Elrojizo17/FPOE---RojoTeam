import tkinter as tk
import tkinter.messagebox as messagebox
from Controladores.registrar_servicio import Registrar_servicio
from .tabla_servicio import TablaServicio

class CrearServicio():
    def __init__(self, menu):
        self.titulos = ['Identificador', 'Nombre Servicio', 'Cédula Cliente', 'Descripción', 'Valor']
        self.columnas = ['id', 'nombre_servicio', 'cedula_cliente', 'descripcion', 'valor']
        data = []
        self.ventana = tk.Toplevel(menu)
        self.tabla = TablaServicio(self.ventana, self.titulos, self.columnas, data)
        self.ventana.focus_set()
        self.ventana.title("Registrar Servicio")
        self.ventana.resizable(0, 0)
        self.controladores = Registrar_servicio(self, self.tabla)

        self.nombre_servicio = tk.StringVar()
        self.cedula_cliente = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.valor = tk.StringVar()
        self.id=tk.StringVar()

        self.crear_interfaz_servicio()

    def crear_interfaz_servicio(self):
        # Título
        self.titulo = tk.Label(self.ventana, text="Registrar Servicio")
        self.titulo.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

        # Nombre del Servicio
        self.lblNombreServicio = tk.Label(self.ventana, text="Nombre del Servicio: ")
        self.lblNombreServicio.grid(row=1, column=0, padx=15, pady=5)
        self.txtNombreServicio = tk.Entry(self.ventana, width=20, textvariable=self.nombre_servicio)
        self.txtNombreServicio.grid(row=1, column=1, padx=15, pady=5)
        self.txtNombreServicio.bind("<KeyRelease>", lambda event: self.controladores.val_nombre_servicio(event, self.txtNombreServicio))

        # Cédula del Cliente
        self.lblCedulaCServicio = tk.Label(self.ventana, text="Cédula del Cliente: ")
        self.lblCedulaCServicio.grid(row=2, column=0, padx=15, pady=5)
        self.txtCedulaServicio = tk.Entry(self.ventana, width=20, textvariable=self.cedula_cliente)
        self.txtCedulaServicio.grid(row=2, column=1, padx=15, pady=5)
        self.txtCedulaServicio.bind("<KeyRelease>", lambda event: self.controladores.val_cedula_servicio(event, self.txtCedulaServicio))

        # Descripción
        self.lblDescripcion = tk.Label(self.ventana, text="Descripción: ")
        self.lblDescripcion.grid(row=3, column=0, padx=15, pady=5)
        self.txtDescripcion = tk.Entry(self.ventana, width=20, textvariable=self.descripcion)
        self.txtDescripcion.grid(row=3, column=1, padx=15, pady=5)
        self.txtDescripcion.bind("<KeyRelease>", lambda event: self.controladores.val_descripcion(event, self.txtDescripcion))

        # Valor
        self.lblValor = tk.Label(self.ventana, text="Valor: ")
        self.lblValor.grid(row=4, column=0, padx=15, pady=5)
        self.txtValor = tk.Entry(self.ventana, width=20, textvariable=self.valor)
        self.txtValor.grid(row=4, column=1, padx=15, pady=5)
        self.txtValor.bind("<KeyRelease>", lambda event: self.controladores.val_valor(event, self.txtValor))

        #ID
        self.lblID=tk.Label(self.ventana, text="ID: ")
        self.lblID.grid(row=5, column=0, padx=15, pady=15)
        self.txtID=tk.Entry(self.ventana, width=20, textvariable=self.id)
        self.txtID.grid(row=5, column=1, padx=15, pady=15)

        # Botones
        self.btnConsultar_todo = tk.Button(self.ventana, text="Consultar todo", command=lambda: self.controladores.boton_consultar_servicio_todo())
        self.btnConsultar_todo.grid(row=6, column=0, padx=15, pady=15)
        
        self.btnGuardar = tk.Button(self.ventana, text="Validar", command=self.controladores.validar_Servicio)
        self.btnGuardar.grid(row=6, column=1, padx=15, pady=15)

        self.btnConsultar_CC = tk.Button(self.ventana, text="Consultar Cédula del Cliente", command=self.controladores.botonFiltrarServicio)
        self.btnConsultar_CC.grid(row=7, column=0, padx=15, pady=15)

        self.btnGuardar = tk.Button(self.ventana, text="Actualizar", command=lambda:self.controladores.actualizarServicio(self.id.get(),self.nombre_servicio.get(),self.cedula_cliente.get(),self.descripcion.get(),self.valor.get()))
        self.btnGuardar.grid(row=7, column=1, padx=15, pady=15)
        

        

        # Advertencias
        self.lblNombreServicioAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblNombreServicioAdvertencia.grid(row=10, column=0, columnspan=2, padx=15, pady=5)

        self.lblCedulaServicioAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblCedulaServicioAdvertencia.grid(row=10, column=0, columnspan=2, padx=15, pady=5)

        self.lblDescripcionAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblDescripcionAdvertencia.grid(row=10, column=0, columnspan=2, padx=15, pady=5)

        self.lblValorAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblValorAdvertencia.grid(row=10, column=0, columnspan=2, padx=15, pady=5)

        # Tabla de servicios
        self.tabla.tabla_S.grid(row=8, column=0, columnspan=2, padx=15, pady=15)
        self.tabla.tabla_S.bind('<<TreeviewSelect>>', self.seleccionar_elementoS)
        self.tabla.tabla_S.bind('<Delete>', self.borrar_elementoS)

    def seleccionar_elementoS(self, event):
        for i in self.tabla.tabla_S.selection():
            valores = self.tabla.tabla_S.item(i)['values']
            self.txtID.delete(0,tk.END)
            self.txtID.insert(0,str(valores[0]))
            self.txtNombreServicio.delete(0, tk.END)
            self.txtNombreServicio.insert(0, str(valores[1]))
            self.txtCedulaServicio.delete(0, tk.END)
            self.txtCedulaServicio.insert(0, str(valores[2]))
            self.txtDescripcion.delete(0, tk.END)
            self.txtDescripcion.insert(0, str(valores[3]))
            self.txtValor.delete(0, tk.END)
            self.txtValor.insert(0, str(valores[4]))

    def borrar_elementoS(self, event):
        for i in self.tabla.tabla_S.selection():
            id_servicio = self.tabla.tabla_S.item(i)['values'][0]  # Obtener el ID del servicio
            self.controladores.eliminar(id_servicio)  # Llamar a la función eliminar con el ID
            self.tabla.tabla_S.delete(i)
