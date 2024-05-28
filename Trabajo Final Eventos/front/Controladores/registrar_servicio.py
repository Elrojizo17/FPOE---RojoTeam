import requests
import tkinter.messagebox as messagebox
from Modelos.servicio import Servicio
from Controladores.controladores import Controlador

class Registrar_servicio():
    def __init__(self, vista, tabla):
        self.vista = vista
        self.tabla = tabla
        self.servicio = Servicio("", "", "", "")
        self.url="http://localhost:8000/v1/servicio"
        self.controlador= Controlador(self.vista)

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
        nombre_servicio = self.vista.txtNombreServicio.get()
        cedula_cliente = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()

        if not (nombre_servicio and cedula_cliente and descripcion and valor):
            messagebox.showerror("Error", "Todos los campos deben estar diligenciados.")
            return

        if not nombre_servicio.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El nombre solo debe contener letras.")
            return

        if not cedula_cliente.isdigit():
            messagebox.showerror("Error", "La cédula solo debe contener números.")
            return

        response = requests.get("http://localhost:8000/v1/cliente")
        if response.status_code != 200:
            messagebox.showerror("Error", "Error al obtener la lista de clientes.")
            return
        clientes = response.json()

        cedula_existe = False
        for cliente in clientes:
            if cliente['cedula'] == int(cedula_cliente):
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

        self.servicio.nombre_servicio.set(nombre_servicio)
        self.servicio.cedula_cliente.set(cedula_cliente)
        self.servicio.descripcion.set(descripcion)
        self.servicio.valor.set(valor)

        data = {
            "nombre_servicio": nombre_servicio,
            "cedula_cliente": cedula_cliente,
            "descripcion": descripcion,
            "valor": valor
        }

        response = requests.post("http://localhost:8000/v1/servicio", data=data)
        print(response.status_code)
        print(response.content)
    
    def actualizarServicio(self, id, nombre_servicio, cedula_cliente, descripcion, valor):
        if not (nombre_servicio and cedula_cliente and descripcion and valor):
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            data = {
                "nombre_servicio": nombre_servicio,
                "cedula_cliente": cedula_cliente,
                "descripcion": descripcion,
                "valor": valor
            }
            response = requests.put(f"{self.url}/{id}/", json=data)
            if response.status_code == 200:
                self.controlador.limpiarcajasServicio()
                messagebox.showinfo("Éxito", "El servicio ha sido actualizado exitosamente")
                self.boton_consultar_servicio_todo()
            elif response.status_code == 404:
                # Intentar crear el servicio si no se encontró durante la actualización
                response = requests.post(self.url, json=data)
                if response.status_code == 201:
                    self.controlador.limpiarcajasServicio()
                    messagebox.showinfo("Éxito", "El servicio no existía, así que fue creado exitosamente")
                else:
                    self.controlador.limpiarcajasServicio()
                    messagebox.showerror("Error", "No se pudo crear el servicio. Detalle: " + response.content.decode())
            else:
                self.controlador.limpiarcajasServicio()
                messagebox.showerror("Error", "No se pudo actualizar el servicio. Detalle: " + response.content.decode())

    def consultar_servicio(self,cedula_cliente):
        resultado = requests.get(self.url + '/' + str(cedula_cliente))

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        if resultado.status_code == 204:
            messagebox.showinfo("Éxito", "Servicio eliminado correctamente.")
            self.boton_consultar_servicio_todo()  # Refresca la tabla después de eliminar
        else:
            messagebox.showerror("Error", "No se pudo eliminar el servicio.")
    
    def consultar_servicio_todo(self, nombre_servicio, cedula, descripcion, valor):
        print("Filtrando con los siguientes valores:")
        print("Nombre Servicio:", nombre_servicio)
        print("Cédula Cliente:", cedula)
        print("Descripción:", descripcion)
        print("Valor:", valor)
        url = self.url
        params = {}
        if nombre_servicio:
            params['nombre_servicio'] = nombre_servicio
        if cedula:  
            params['cedula'] = cedula  # Cambiado a 'cedula' en lugar de 'cedula_cliente'
        if descripcion:
            params['descripcion'] = descripcion
        if valor:
            params['valor'] = valor
        if params:
            url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])
        print("URL de consulta:", url)
        resultado = requests.get(url)

        if resultado.status_code == 200 and resultado.text:
            return resultado.json()  
        else:
            print("La solicitud no obtuvo una respuesta válida")
            return []
    def boton_consultar_servicio(self, cedula_cliente):
        resultado= self.consultar_ciente(cedula_cliente)
        print(resultado)
        if resultado:
            data=[(resultado.get(id), resultado.get('nombre_servicio'),resultado.get('cedula_cliente'),resultado.get('descripcion'), resultado.get('valor'))]
            self.treeview_servicio.delete(*self.treeview_servicio.get_children())

    def boton_consultar_servicio_todo(self):
        self.controlador.limpiarcajasServicio()
        nombre_servicio= self.vista.txtNombreServicio.get()
        cedula_cliente= self.vista.txtCedulaServicio.get()
        descripcion= self.vista.txtDescripcion.get()
        valor= self.vista.txtValor.get()
        resultados= self.consultar_servicio_todo(nombre_servicio, cedula_cliente, descripcion, valor)
        print(resultados)
        data=[]
        for elemento in resultados:
            data.append((elemento.get('id'),elemento.get('nombre_servicio'),elemento.get('cedula_cliente'),elemento.get('descripcion'),elemento.get('valor')))
            self.mostrar_resultados(resultados)
        self.tabla.refrescar_tablaS(data)
    

    def mostrar_resultados(self, resultados):
        for resultado in resultados:
            print(resultado)

    def botonFiltrarServicio(self):
        nombre_servicio = self.vista.txtNombreServicio.get()
        cedula_cliente = self.vista.txtCedulaServicio.get()
        descripcion = self.vista.txtDescripcion.get()
        valor = self.vista.txtValor.get()
        print("Filtrando con los siguientes valores:")
        print("Nombre Servicio:", nombre_servicio)
        print("Cédula Cliente:", cedula_cliente)
        print("Descripción:", descripcion)
        print("Valor:", valor)
        resultados = self.consultar_servicio_todo(nombre_servicio, cedula_cliente, descripcion, valor)
        print("Resultados obtenidos:")
        print(resultados)
        data = []
        for elemento in resultados:
            data.append((elemento.get('id'), elemento.get('nombre_servicio'), elemento.get('cedula_cliente'), elemento.get('descripcion'), elemento.get('valor')))
        print("Datos a mostrar en la tabla:")
        print(data)
        self.tabla.refrescar_tablaS(data)