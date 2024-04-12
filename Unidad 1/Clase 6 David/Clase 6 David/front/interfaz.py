import tkinter
import requests
from tkinter import messagebox as mb
from tkinter.messagebox import askyesno, showerror, showinfo


ventana = tkinter.Tk()
ventana.title("Moto")
ventana.geometry("300x300")
ventana.resizable(0, 0)

marca = tkinter.StringVar()
cilindraje = tkinter.IntVar()
modelo = tkinter.IntVar()
color = tkinter.StringVar()


def validar_marca(marca):
    if not marca.isalpha():
        print("¡Error! Solo se permiten letras.")
    return marca.isalpha() or marca == ""  
validacion_marca = ventana.register(validar_marca)

def validar_cilindraje(cilindraje):
    if not cilindraje.isdigit():
        print("¡Error! Solo se permiten letras.")
    return cilindraje.isdigit() or cilindraje == ""  
validacion_cilindraje = ventana.register(validar_cilindraje)

def validar_modelo(modelo):
    if not modelo.isdigit():
        print("¡Error! Solo se permiten letras.")
    return modelo.isdigit() or modelo == ""  
validacion_modelo = ventana.register(validar_modelo)

def validar_color(color):
    if not color.isalpha():
        print("¡Error! Solo se permiten letras.")
    return color.isalpha() or color == ""  
validacion_color = ventana.register(validar_color)


def diligenciar():
    if not (txtMarca.get() and txtCilindraje.get() and txtModelo.get() and txtColor.get()):
        showerror("Error", "Todos los campos deben estar completos")
        return
    
    showinfo("Exito", "Firma esta bien")

    data = {
        "marca": marca.get(),
        "cilindraje": cilindraje.get(),
        "modelo": modelo.get(),
        "color": color.get()
    }

    response = requests.post("http://localhost:8000/v1/moto", data=data)

    print(response.status_code)

    print(response.content)

    #showinfo("Exito", "Firma esta bien")


label1 = tkinter.Label(ventana, text="Marca")
label1.grid(column=0, row=0, padx=15, pady=15)
txtMarca = tkinter.Entry(ventana, width=20, textvariable=marca, validate="key", validatecommand=(validacion_marca, '%P'))
txtMarca.grid(column=1, row=0)

label2 = tkinter.Label(ventana, text="cilindraje")
label2.grid(column=0, row=1, padx=15, pady=15)
txtCilindraje = tkinter.Entry(ventana, width=20, textvariable=cilindraje,  validate="key", validatecommand=(validacion_cilindraje, '%P'))
txtCilindraje.grid(column=1, row=1)

label3 = tkinter.Label(ventana, text="Modelo")
label3.grid(column=0, row=2, padx=15, pady=15)
txtModelo = tkinter.Entry(ventana, width=20, textvariable=modelo, validate="key", validatecommand=(validacion_modelo, '%P'))
txtModelo.grid(column=1, row=2)

label4 = tkinter.Label(ventana, text="Color")
label4.grid(column=0, row=3, padx=15, pady=15)
txtColor = tkinter.Entry(ventana, width=20, textvariable=color, validate="key", validatecommand=(validacion_color, '%P'))
txtColor.grid(column=1, row=3)


def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseea cerrar la App?"):
        ventana.destroy()

def limpiarcajas():
    marca.set("")
    cilindraje.set("")
    modelo.set("")
    color.set("")

    txtMarca.focus_set()

boton2 = tkinter.Button(ventana, text="Limpiar", command=limpiarcajas)
boton2.grid(column=0, row=5, padx=15, pady=15)

boton1 = tkinter.Button(ventana, text="Salir", command=el_usuario_quiere_salir)
boton1.grid(column=1, row=5, padx=15, pady=15)

boton3 = tkinter.Button(ventana, text="Validar", command=diligenciar)
boton3.grid(column=3, row=5, padx=15, pady=15)

ventana.mainloop()



"""data = {
    "marca": marca.get(),
    "cilindraje": cilindraje.get(),
    "modelo": modelo.get(),
    "color": color.get()
}

response = requests.post("http://localhost:8000/v1/moto", data=data)

print(response.status_code)

print(response.content)"""