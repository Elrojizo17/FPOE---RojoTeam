import tkinter.messagebox as messagebox
import requests
from vistas.tabla import Tabla
import tkinter as tk
import tkinter

class Controlador:
    def __init__(self, vista, tabla):
        self.vista = vista
        self.tabla = tabla
        self.url = "http://localhost:8000/v1/moto"

    def el_usuario_quiere_salir(self):
        if messagebox.askyesno("Salir de la Aplicación", "¿Seguro que desea cerrar la App?"):
            self.vista.ventana.destroy()

    def validar_marca(self, marca):
        if not marca.isalpha():
            messagebox.showerror("Error", "¡Error! La marca solo puede contener letras.")
            return False
        return True

    def validar_cilindraje(self, cilindraje):
        if not cilindraje.isdigit():
            messagebox.showerror("Error", "¡Error! El cilindraje debe ser un número entero.")
            return False
        return True

    def validar_modelo(self, modelo):
        if not modelo.isdigit():
            messagebox.showerror("Error", "¡Error! El modelo debe ser un número entero.")
            return False
        return True

    def validar_color(self, color):
        if not color.isalpha():
            messagebox.showerror("Error", "¡Error! El color solo puede contener letras.")
            return False
        return True


    def diligenciar(self):
        marca = self.vista.txtMarca.get()
        cilindraje = self.vista.txtCilindraje.get()
        modelo = self.vista.txtModelo.get()
        color = self.vista.txtColor.get()

        if not (marca and cilindraje and modelo and color):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return

        if not (self.validar_marca(marca) and self.validar_cilindraje(cilindraje) and
                self.validar_modelo(modelo) and self.validar_color(color)):
            return

        messagebox.showinfo("Exito", "Firma, está bien")

        data = {
            "marca": marca,
            "cilindraje": cilindraje,
            "modelo": modelo,
            "color": color
        }

        try:
            response = requests.post("http://localhost:8000/v1/moto", data=data)
            print(response.status_code)
            print(response.content)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al enviar los datos al servidor: {e}")

        self.vista.txtMarca.delete(0, tkinter.END)
        self.vista.txtCilindraje.delete(0, tkinter.END)
        self.vista.txtModelo.delete(0, tkinter.END)
        self.vista.txtColor.delete(0, tkinter.END)
        self.vista.txtId.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()

    def boton_consultar(self, id):
        data = []
        resultado = self.consultar(id)

        if isinstance(resultado, dict):
            data.append((resultado.get('id'), resultado.get('marca'), resultado.get('cilindraje'), resultado.get('modelo'), resultado.get('color')))

        self.vista.tabla.refrescar(data)

        self.vista.txtId.delete(0, tkinter.END)

        self.vista.txtMarca.delete(0, tkinter.END)
        self.vista.txtCilindraje.delete(0, tkinter.END)
        self.vista.txtModelo.delete(0, tkinter.END)
        self.vista.txtColor.delete(0, tkinter.END)
        self.vista.txtId.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()


    def boton_consultar_todo(self):
        marca = self.vista.txtMarca.get()
        cilindraje = self.vista.txtCilindraje.get()
        modelo = self.vista.txtModelo.get()
        color = self.vista.txtColor.get()
        data = []
        resultados = self.consultar_todo(marca, cilindraje, modelo, color)
        for elemento in resultados:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('cilindraje'), elemento.get('modelo'), elemento.get('color')))
        self.vista.tabla.refrescar(data)


    def boton_filtar(self):
        marca = self.vista.txtMarca.get()
        cilindraje = self.vista.txtCilindraje.get()
        modelo = self.vista.txtModelo.get()
        color = self.vista.txtColor.get()
        resultados = self.consultar_todo(marca, cilindraje, modelo, color)
        self.mostrar_resultados(resultados)
        data = []
        for elemento in resultados:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('cilindraje'), elemento.get('modelo'), elemento.get('color')))
        self.vista.tabla.refrescar(data)
        self.vista.txtMarca.delete(0, tkinter.END)
        self.vista.txtCilindraje.delete(0, tkinter.END)
        self.vista.txtModelo.delete(0, tkinter.END)
        self.vista.txtColor.delete(0, tkinter.END)
        self.vista.txtId.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()

    def mostrar_resultados(self, resultados):
        for resultado in resultados:
            print(resultado)

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code

    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()

    def consultar_todo(self, marca, cilindraje, modelo, color):
        url = self.url + "?"

        if marca:
            url += "marca=" + marca + "&"
        if cilindraje:
            url += "cilindraje=" + cilindraje + "&"
        if modelo:
            url += "modelo=" + modelo + "&"
        if color:
            url += "color=" + color + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()
    

    def actualizar(self, id, marca, cilindraje, modelo, color):
        id = self.vista.txtId.get()
        marca = self.vista.txtMarca.get()
        cilindraje = self.vista.txtCilindraje.get()
        modelo = self.vista.txtModelo.get()
        color = self.vista.txtColor.get()
        
        if not (marca and cilindraje and modelo and color):
            messagebox.showerror("Error", "Todos los campos deben estar completos")
            return

        if not (self.validar_marca(marca) and self.validar_cilindraje(cilindraje) and
                self.validar_modelo(modelo) and self.validar_color(color)):
            return

        data = {
            "marca": marca,
            "cilindraje": cilindraje,
            "modelo": modelo,
            "color": color
        }

        url = f"{self.url}/{id}/"
        print(f"URL: {url}")
        print(f"Data: {data}")

        response = requests.put(url, json=data)
        messagebox.showinfo("Éxito", "Actualización exitosa")

        self.vista.txtMarca.delete(0, tkinter.END)
        self.vista.txtCilindraje.delete(0, tkinter.END)
        self.vista.txtModelo.delete(0, tkinter.END)
        self.vista.txtColor.delete(0, tkinter.END)
        self.vista.txtId.delete(0, tkinter.END)
        self.vista.txtMarca.focus_set()

        self.boton_consultar_todo()



