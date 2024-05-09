import tkinter.messagebox as messagebox

class Controlador:
    def __init__(self, vista):
        self.vista = vista

    def el_usuario_quiere_salir(self):
        if messagebox.askyesno("Salir de la Aplicación", "¿Seguro que desea cerrar la App?"):
            self.vista.ventana.destroy()