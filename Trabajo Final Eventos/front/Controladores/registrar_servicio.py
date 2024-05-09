import requests
import tkinter.messagebox as messagebox
from Modelos.servicio import Servicio
class Registrar_servicio():
    def __init__(self, vista):
        self.vista = vista
        self.servicio = Servicio("", "", "", "")

    def val_nombre_servicio(self, event, widget):
        nombre_servicio_val = widget.get()
        if not nombre_servicio_val.replace(" ", "").isalpha():
            self.vista.lblNombreServicioAdvertencia.config(text="El nombre sólo debe contener letras.", fg="red")
        else:
            self.vista.lblNombreServicioAdvertencia.config(text="")
    
    def val_cedula_servicio(self, event, widget):
        cedula_servicio_val = widget.get()
        if not cedula_servicio_val.isdigit():
            self.vista.lblCedulaServicioAdvertencia.config(text="La cédula debe contener números únicamente.", fg="red")
        else:
            self.vista.lblCedulaServicioAdvertencia.config(text="")

    def val_descripcion(self, event, widget):
        descripcion_val = widget.get()
        if not descripcion_val.replace(" ", "").isalnum():
            self.vista.lblDescripcionAdvertencia.config(text="La descripción solo debe contener letras, números y/o espacios.", fg="red")
        else:
            self.vista.lblDescripcionAdvertencia.config(text="")

    def val_valor(self, event, widget):
        valor_val = widget.get()
        if not valor_val.isdigit():
            self.vista.lblValorAdvertencia.config(text="El valor debe contener números únicamente.", fg="red")
        else:
            self.vista.lblValorAdvertencia.config(text="")

    def validar_Servicio(self):
        nombre = self.vista.txtNombreServicio.get()
        cedula = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        if not (nombre and cedula and descripcion and valor):
            messagebox.showerror("Error", "Todos los campos deben estar diligenciados.")
            return

        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not cedula.isdigit():
            messagebox.showerror("Error", "La cédula solo debe contener números.")
            return

        response = requests.get("http://localhost:8000/v1/cliente")
        if response.status_code != 200:
            messagebox.showerror("Error", "Error al obtener la lista de clientes.")
            return
        clientes = response.json()

        cedula_existe = False
        for cliente in clientes:
            if cliente['cedula'] == int(cedula):
                cedula_existe = True
                break

        if not cedula_existe:
            messagebox.showerror("Error", "La cédula ingresada no corresponde a un cliente registrado.")
            return

        if not descripcion.replace(" ", "").isalnum():
            return

        if not valor.isdigit():
            messagebox.showerror("Error", "El valor debe ser un número.")
            return

        messagebox.showinfo("Éxito", "Servicio Registrado correctamente.")

        self.servicio.nombre_servicio.set(nombre)
        self.servicio.cedula.set(cedula)
        self.servicio.descripcion.set(descripcion)
        self.servicio.valor.set(valor)

        data = {
            "nombre_servicio": nombre,
            "cedula_cliente": cedula,
            "descripcion": descripcion,
            "valor": valor
        }

        response = requests.post("http://localhost:8000/v1/servicio", data=data)
        print(response.status_code)
        print(response.content)