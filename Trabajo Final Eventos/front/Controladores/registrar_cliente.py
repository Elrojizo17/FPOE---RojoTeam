import requests
import tkinter.messagebox as messagebox
from Modelos.cliente import Cliente

class Registrar_cliente():
    def __init__(self, vista):
        self.vista = vista
        self.cliente = Cliente("", "", "", "", "")

    def val_nombre(self, event, widget):
        nombre_val = widget.get()
        if not nombre_val.replace(" ", "").isalpha():
            self.vista.lblNombreAdvertencia.config(text="El nombre solo debe contener letras.", fg="red")
        else:
            self.vista.lblNombreAdvertencia.config(text="")

    def val_apellido(self, event, widget): 
        apellido_val = widget.get()         
        if not apellido_val.replace(" ", "").isalpha():
            self.vista.lblApellidoAdvertencia.config(text="El apellido solo debe contener letras.", fg="red")
        else:
            self.vista.lblApellidoAdvertencia.config(text="")
    
    def val_cedula(self, event, widget):
        cedula_val = widget.get()
        if not cedula_val.isdigit():
            self.vista.lblCedulaAdvertencia.config(text="Error: La cédula debe ser un número.", fg="red")
        else:
            self.vista.lblCedulaAdvertencia.config(text="")
    
    def val_telefono(self, event, widget):
        telefono_val = widget.get()
        if not telefono_val.isdigit():
            self.vista.lblTelefonoAdvertencia.config(text="Error: El teléfono debe ser un número.", fg="red")
        else:
            self.vista.lblTelefonoAdvertencia.config(text="")

    def val_correo(self, event, widget): 
        correo_val = widget.get()         
        if "@" not in correo_val:
            self.vista.lblCorreoAdvertencia.config(text="El correo debe incluir un arroba.", fg="red")
        else:
            self.vista.lblCorreoAdvertencia.config(text="")

    def validar(self):
        nombre = self.vista.txtNombre.get()
        apellido = self.vista.txtApellido.get()
        cedula = self.vista.txtCedula.get()
        telefono = self.vista.txtTelefono.get()
        correo = self.vista.txtCorreo.get()

        if not (nombre and apellido and cedula and telefono and correo):
            messagebox.showerror("Error", "Todos los campos deben estar completos.")
            return

        if not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not apellido.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El apellido solo debe contener letras.")
            return

        if not cedula.isdigit():
            messagebox.showerror("Error", "La cédula debe ser un número.")
            return
        
        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe ser un número.")
            return
        
        if "@" not in correo:
            messagebox.showerror("Error", "El correo no tiene arroba.")
            return

        messagebox.showinfo("Éxito", "Cliente Registrado Exitosamente.")

        self.cliente.nombre.set(nombre)
        self.cliente.apellido.set(apellido)
        self.cliente.cedula.set(cedula)
        self.cliente.telefono.set(telefono)
        self.cliente.correo.set(correo)

        data = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "telefono": telefono,
            "correo": correo
        }

        response = requests.post("http://localhost:8000/v1/cliente", data=data)
        print(response.status_code)
        print(response.content)