import requests
import tkinter.messagebox as mb
from Modelos.cliente import Cliente
import requests
from Controladores.controladores import Controlador 
import tkinter.messagebox as messagebox

class Registrar_cliente():
    def __init__(self, vista, tabla):
        self.vista = vista
        self.tabla=tabla
        self.controlador= Controlador(self.vista)
        self.cliente = Cliente("", "", "", "", "")
        self.url="http://192.168.62.118:8000/v1/cliente"

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
            mb.showerror("Error", "Todos los campos deben estar completos.")
            return

        if not nombre.replace(" ", "").isalpha():
            mb.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not apellido.replace(" ", "").isalpha():
            mb.showerror("Error", "El apellido solo debe contener letras.")
            return

        if not cedula.isdigit():
            mb.showerror("Error", "La cédula debe ser un número.")
            return
        
        if not telefono.isdigit():
            mb.showerror("Error", "El teléfono debe ser un número.")
            return
        
        if "@" not in correo:
            mb.showerror("Error", "El correo no tiene arroba.")
            return

        mb.showinfo("Éxito", "Cliente Registrado Exitosamente.")

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

        response = requests.post("http://192.168.62.118:8000/v1/cliente", data=data)
        print(response.status_code)
        print(response.content)


    def validar(self):
        nombre = self.vista.txtNombre.get()
        apellido = self.vista.txtApellido.get()
        cedula = self.vista.txtCedula.get()
        telefono = self.vista.txtTelefono.get()
        correo = self.vista.txtCorreo.get()

        if not (nombre and apellido and cedula and telefono and correo):
            mb.showerror("Error", "Todos los campos deben estar completos.")
            return

        if not nombre.replace(" ", "").isalpha():
            mb.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not apellido.replace(" ", "").isalpha():
            mb.showerror("Error", "El apellido solo debe contener letras.")
            return

        if not cedula.isdigit():
            mb.showerror("Error", "La cédula debe ser un número.")
            return
        
        if not telefono.isdigit():
            mb.showerror("Error", "El teléfono debe ser un número.")
            return
        
        if "@" not in correo:
            mb.showerror("Error", "El correo no tiene arroba.")
            return

        mb.showinfo("Éxito", "Cliente Registrado Exitosamente.")

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

        response = requests.post("http://192.168.62.118:8000/v1/cliente", data=data)
        print(response.status_code)
        print(response.content)


    def actualizar(self, id, nombre, apellido, cedula, telefono, correo):
        if not (nombre and apellido and cedula and telefono and correo):
            mb.showerror("Error", "Debe llenar todos los campos.")
            return

        data = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "telefono": telefono,
            "correo": correo
        }

        try:
            response = requests.put(f"{self.url}/{id}/", json=data)
            print("URL de la solicitud:", response.request.url)  # Imprimir la URL utilizada para la solicitud
            print("Datos enviados:", data)  # Imprimir los datos enviados
            print("Código de respuesta:", response.status_code)  # Imprimir el código de respuesta

            if response.status_code == 200:
                self.controlador.limpiarcajasCliente()
                mb.showinfo("Éxito", "El objeto ha sido actualizado exitosamente.")
                self.boton_consultar_cliente_todo()
            elif response.status_code == 404:
                # Intentar crear el objeto si no se encontró durante la actualización
                response = requests.post(self.url, json=data)
                if response.status_code == 201:
                    self.controlador.limpiarcajasCliente()
                    mb.showinfo("Éxito", "El objeto no existía, así que fue creado exitosamente.")
                else:
                    print("Error de creación:", response.status_code, response.content.decode())  # Depuración adicional
                    self.controlador.limpiarcajasCliente()
                    mb.showerror("Error", "No se pudo crear el objeto. Detalle: " + response.content.decode())
            else:
                print("Error de actualización:", response.status_code, response.content.decode())  # Depuración adicional
                self.controlador.limpiarcajasCliente()
                mb.showerror("Error", "No se pudo actualizar el objeto. Detalle: " + response.content.decode())
        except requests.RequestException as e:
            print("Excepción de solicitud:", str(e))  # Depuración adicional
            mb.showerror("Error", "Hubo un problema con la solicitud: " + str(e))

    def consultar_ciente(self,cedula):
        resultado = requests.get(self.url + '/' + str(cedula))
        return resultado.json()
    

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        if resultado.status_code == 204:
            messagebox.showinfo("Éxito", "Servicio eliminado correctamente.")
            self.boton_consultar_cliente_todo()  # Refresca la tabla después de eliminar
        else:
            messagebox.showerror("Error", "No se pudo eliminar el servicio.")

        
    def consultar_cliente_todo(self, nombre, apellido, cedula, telefono, correo):
        url = self.url
        params = {}
        if nombre:
            params["nombre"] = nombre
        if apellido:
            params["apellido"] = apellido
        if cedula:
            params["cedula"] = cedula
        if telefono:
            params["telefono"] = telefono
        if correo:
            params["correo"] = correo
        if params:
            url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])
        print(url)
        resultado = requests.get(url)

        if resultado.status_code == 200 and resultado.text:
            return resultado.json()  # Llamar al método json()
        else:
            print(url)
            print("La solicitud no obtuvo una respuesta válida")
            return []

    def boton_consultar_cliente(self, cedula):
        resultado= self.consultar_ciente(cedula)
        print(resultado)
        if resultado:
            data=[(resultado.get(id), resultado.get('nombre'),resultado.get('apellido'),resultado.get('cedula'), resultado.get('telefono'), resultado.get('correo'))]
            self.tabla.refrescar_tablaC()

    def boton_consultar_cliente_todo(self):
        self.controlador.limpiarcajasCliente()
        nombre= self.vista.txtNombre.get()
        apellido= self.vista.txtApellido.get()
        cedula= self.vista.txtCedula.get()
        telefono= self.vista.txtTelefono.get()
        correo= self.vista.txtCorreo.get()
        resultados= self.consultar_cliente_todo(nombre, apellido, cedula, telefono, correo)
        print(resultados)
        data=[]
        for elemento in resultados:
            data.append((elemento.get('id'),elemento.get('nombre'),elemento.get('apellido'),elemento.get('cedula'),elemento.get('telefono'),elemento.get('correo')))
            self.mostrar_resultados(resultados)
        self.tabla.refrescar_tablaC(data)
        

    def mostrar_resultados(self, resultados):
        for resultado in resultados:
            print(resultado)

    def botonFiltrarCliente(self):
        nombre=self.vista.txtNombre.get()
        apellido=self.vista.txtApellido.get()
        cedula=self.vista.txtCedula.get()
        telefono=self.vista.txtTelefono.get()
        correo=self.vista.txtCorreo.get()
        resultados=self.consultar_cliente_todo(nombre, apellido, cedula, telefono,correo)
        data=[]
        for elemento in resultados:
            data.append((elemento.get('id'),elemento.get('nombre'),elemento.get('apellido'),elemento.get('cedula'),elemento.get('telefono'),elemento.get('correo')))
        self.tabla.refrescar_tablaC(data)

