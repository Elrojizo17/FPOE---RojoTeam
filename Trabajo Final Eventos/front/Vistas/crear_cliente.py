import tkinter as tk
import tkinter.messagebox as messagebox
from Controladores.registrar_cliente import Registrar_cliente
from .tabla_cliente import TablaCliente

class CrearCliente():
    def __init__(self, menu):
        self.titulos=['Identificador','Nombre','Apellido','Cédula','Teléfono','Correo']
        self.columnas=['Id','nombre','apellido','cedula','telefono','correo']
        data=[]
        self.ventana = tk.Toplevel(menu)
        self.tabla=TablaCliente(self.ventana, self.titulos, self.columnas, data)
        self.ventana.focus_set()
        self.ventana.title("Registrar Cliente")
        self.ventana.resizable(0, 0)
        self.controladores = Registrar_cliente(self, self.tabla)
        self.nombre= tk.StringVar()
        self.apellido=tk.StringVar()
        self.cedula=tk.StringVar()
        self.telefono=tk.StringVar()
        self.correo=tk.StringVar()
        self.id=tk.StringVar()

        self.crear_interfaz_cliente()

    def crear_interfaz_cliente(self):
        self.titulo = tk.Label(self.ventana, text="Registrar Cliente")
        self.titulo.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

        # Nombre
        self.lblNombre = tk.Label(self.ventana, text="Nombre: ")
        self.lblNombre.grid(row=1, column=0, padx=15, pady=15)
        self.txtNombre = tk.Entry(self.ventana, width=20, textvariable=self.nombre)
        self.txtNombre.grid(row=1, column=1, padx=15, pady=15)
        self.txtNombre.bind("<KeyRelease>", lambda event: self.controladores.val_nombre(event, self.txtNombre))

        # Apellido
        self.lblApellido = tk.Label(self.ventana, text="Apellido: ")
        self.lblApellido.grid(row=3, column=0, padx=15, pady=15)
        self.txtApellido = tk.Entry(self.ventana, width=20, textvariable=self.apellido)
        self.txtApellido.grid(row=3, column=1, padx=15, pady=15)
        self.txtApellido.bind("<KeyRelease>", lambda event: self.controladores.val_apellido(event, self.txtApellido))

        # Cédula
        self.lblCedula = tk.Label(self.ventana, text="Cédula: ")
        self.lblCedula.grid(row=5, column=0, padx=15, pady=15)
        self.txtCedula = tk.Entry(self.ventana, width=20, textvariable=self.cedula)
        self.txtCedula.grid(row=5, column=1, padx=15, pady=15)
        self.txtCedula.bind("<KeyRelease>", lambda event: self.controladores.val_cedula(event, self.txtCedula))

        # Teléfono
        self.lblTelefono = tk.Label(self.ventana, text="Teléfono: ")
        self.lblTelefono.grid(row=7, column=0, padx=15, pady=15)
        self.txtTelefono = tk.Entry(self.ventana, width=20, textvariable=self.telefono)
        self.txtTelefono.grid(row=7, column=1, padx=15, pady=15)
        self.txtTelefono.bind("<KeyRelease>", lambda event: self.controladores.val_telefono(event, self.txtTelefono))

        # Correo
        self.lblCorreo = tk.Label(self.ventana, text="Correo: ")
        self.lblCorreo.grid(row=9, column=0, padx=15, pady=15)
        self.txtCorreo = tk.Entry(self.ventana, width=20, textvariable=self.correo)
        self.txtCorreo.grid(row=9, column=1, padx=15, pady=15)
        self.txtCorreo.bind("<KeyRelease>", lambda event: self.controladores.val_correo(event, self.txtCorreo))

        #ID
        self.lblID=tk.Label(self.ventana, text="ID: ")
        self.lblID.grid(row=10, column=0, padx=15, pady=15)
        self.txtID=tk.Entry(self.ventana, width=20, textvariable=self.id)
        self.txtID.grid(row=10, column=1, padx=15, pady=15)

        # Buttons
        self.btnGuardar = tk.Button(self.ventana, text="Validar", command=self.controladores.validar)
        self.btnGuardar.grid(row=11, column=1, padx=15, pady=15)
        self.btnConsultar_cliente=tk.Button(self.ventana, text="Consultar Cédula", command=self.controladores.botonFiltrarCliente())
        self.btnConsultar_cliente.grid(row=11, column=0, padx=15, pady=15)
        self.btnConsultar_todo = tk.Button(self.ventana, text="Consultar todo", command=lambda: self.controladores.boton_consultar_cliente_todo())
        self.btnConsultar_todo.grid(row=12, column=0, padx=15, pady=15)
        self.Actualizar_cliente = tk.Button(self.ventana, text="Actualizar", command=lambda: self.controladores.actualizar(self.id.get(),self.nombre.get(),self.apellido.get(),self.cedula.get(),self.telefono.get(),self.correo.get()))
        self.Actualizar_cliente.grid(row=12, column=1, padx=15, pady=15)

        # Advertencias
        self.lblNombreAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblNombreAdvertencia.grid(row=20, column=0, columnspan=2, padx=15, pady=5)
        self.lblApellidoAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblApellidoAdvertencia.grid(row=20, column=0, columnspan=2, padx=15, pady=5)
        self.lblCedulaAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblCedulaAdvertencia.grid(row=20, column=0, columnspan=2, padx=15, pady=5)
        self.lblTelefonoAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblTelefonoAdvertencia.grid(row=20, column=0, columnspan=2, padx=15, pady=5)
        self.lblCorreoAdvertencia = tk.Label(self.ventana, text="", fg="red")
        self.lblCorreoAdvertencia.grid(row=20, column=0, columnspan=2, padx=15, pady=5)

    

        self.tabla.tabla_C.grid(row=14, column=0, columnspan=2)
        self.tabla.tabla_C.bind('<<TreeviewSelect>>',self.seleccionar_elementoC)
        self.tabla.tabla_C.bind('<Delete>',self.borrar_elementoC)

    def seleccionar_elementoC(self,event):
        for i in self.tabla.tabla_C.selection():
            valores = self.tabla.tabla_C.item(i)['values']
            self.txtID.delete(0,tk.END)
            self.txtID.insert(0,str(valores[0]))
            self.txtNombre.delete(0,tk.END)
            self.txtNombre.insert(0,str(valores[1]))
            self.txtApellido.delete(0,tk.END)
            self.txtApellido.insert(0,str(valores[2]))
            self.txtCedula.delete(0,tk.END)
            self.txtCedula.insert(0,str(valores[3]))
            self.txtTelefono.delete(0,tk.END)
            self.txtTelefono.insert(0,str(valores[4]))
            self.txtCorreo.delete(0,tk.END)
            self.txtCorreo.insert(0,str(valores[5]))

    def borrar_elementoC(self, event):
        for i in self.tabla.tabla_C.selection():
            cliente_id = self.tabla.tabla_C.item(i)['values'][0]  # Obtener el ID del cliente
            self.controladores.eliminar(cliente_id)  # Llamar a la función eliminar con el ID
            self.tabla.tabla_C.delete(i)