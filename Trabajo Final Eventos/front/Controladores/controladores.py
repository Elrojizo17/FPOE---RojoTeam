import tkinter.messagebox as messagebox
from Modelos.cliente import Cliente

class Controlador:
    def __init__(self, vista):
        self.vista = vista

    def el_usuario_quiere_salir(self):
        if messagebox.askyesno("Salir de la Aplicación", "¿Seguro que desea cerrar la App?"):
            self.vista.ventana.destroy()

    def limpiarcajasCliente(self):
        self.vista.nombre.set("")
        self.vista.apellido.set("")
        self.vista.cedula.set("")
        self.vista.telefono.set("")
        self.vista.correo.set("")

    
    def limpiarcajasServicio(self):
        self.vista.nombre_servicio.set("")
        self.vista.cedula_cliente.set("")
        self.vista.descripcion.set("")
        self.vista.valor.set("")