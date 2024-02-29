import tkinter
from tkinter import messagebox as mb 
from tkinter.messagebox import askyesno

ventana = tkinter.Tk()
ventana.title("Wiwuwiwuuw")
ventana.geometry("300x300")
ventana.resizable(0, 0)

nombre = tkinter.StringVar()
apellido = tkinter.StringVar()
correo = tkinter.StringVar()
edad = tkinter.StringVar()
fecha = tkinter.StringVar()

def validar_nombre(nombre):
    if not nombre.isalpha():
        print("¡Error! Solo se permiten letras.")
    return nombre.isalpha() or nombre == ""  
validacion_nombre = ventana.register(validar_nombre)

def validar_apellido(apellido):
    if not apellido.isalpha():
        print("¡Error! Solo se permiten letras.")
    return apellido.isalpha() or apellido == ""  
validacion_apellido = ventana.register(validar_apellido)

def validar_edad(edad):
    if not edad.isdigit():
        print("¡Error! Solo se permiten números.")
        return False

    if len(edad) > 3:
        print("¡Error! La edad debe tener como máximo 3 caracteres.")
        return False

    return True

validacion_edad = ventana.register(validar_edad)

def validar_correo(correo):
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.")
    if not set(correo).issubset(caracteres_permitidos):
        print("¡Error! Solo se permiten letras, números, @ y punto (.) en el correo electrónico.")
        return False
    return True
validacion_correo = ventana.register(validar_correo)


def validar_fecha(fecha):
    caracteres_permitidos = set("0123456789/")
    if not set(fecha).issubset(caracteres_permitidos):
        print("¡Error! Solo se permiten números y / en la fecha.")
        return False

    if len(fecha.replace("/", "")) > 8:
        print("¡Error! La fecha debe tener como máximo 8 caracteres (DD/MM/AAAA).")
        return False

    return True

validacion_fecha = ventana.register(validar_fecha)

def insertar_barra(event):
    current_text = txtFecha.get()
    if len(current_text) == 2 or len(current_text) == 5:
        txtFecha.insert(tkinter.END, '/')

label1 = tkinter.Label(ventana, text="Nombre")
label1.grid(column=0, row=0, padx=15, pady=15)
txtNombre = tkinter.Entry(ventana, width=20, textvariable=nombre, validate="key", validatecommand=(validacion_nombre, '%P'))
txtNombre.grid(column=1, row=0)

label2 = tkinter.Label(ventana, text="Apellido")
label2.grid(column=0, row=1, padx=15, pady=15)
txtApellido = tkinter.Entry(ventana, width=20, textvariable=apellido,  validate="key", validatecommand=(validacion_apellido, '%P'))
txtApellido.grid(column=1, row=1)

label3 = tkinter.Label(ventana, text="Correo")
label3.grid(column=0, row=2, padx=15, pady=15)
txtCorreo = tkinter.Entry(ventana, width=20, textvariable=correo, validate="key", validatecommand=(validacion_correo, '%P'))
txtCorreo.grid(column=1, row=2)

label4 = tkinter.Label(ventana, text="Edad")
label4.grid(column=0, row=3, padx=15, pady=15)
txtEdad = tkinter.Entry(ventana, width=20, textvariable=edad, validate="key", validatecommand=(validacion_edad, '%P'))
txtEdad.grid(column=1, row=3)

label5 = tkinter.Label(ventana, text="Fecha de Nacimiento")
label5.grid(column=0, row=4, padx=15, pady=15)
txtFecha = tkinter.Entry(ventana, width=20, textvariable=fecha, validate="key", validatecommand=(validacion_fecha, '%P'))
txtFecha.grid(column=1, row=4)
txtFecha.bind("<KeyRelease>", insertar_barra)

def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseea cerrar la App?"):
        ventana.destroy()

def limpiarcajas():
    nombre.set("")
    apellido.set("")
    correo.set("")
    edad.set("")
    fecha.set("")
    txtNombre.focus_set()

boton2 = tkinter.Button(ventana, text="Limpiar", command=limpiarcajas)
boton2.grid(column=0, row=5, padx=15, pady=15)

boton1 = tkinter.Button(ventana, text="Salir", command=el_usuario_quiere_salir)
boton1.grid(column=1, row=5, padx=15, pady=15)

ventana.mainloop()
