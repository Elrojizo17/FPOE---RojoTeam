import tkinter
from tkinter import messagebox as mb 
from tkinter.messagebox import askyesno

ventana = tkinter.Tk()
ventana.title("Formulario")
ventana.geometry("420x460")
ventana.resizable(0, 0)
ventana.iconbitmap("UnivalleICO.ico")

nombre = tkinter.StringVar()
apellido = tkinter.StringVar()
correo = tkinter.StringVar()
edad = tkinter.StringVar()
fecha = tkinter.StringVar()

def validar_nombre(event):
    nombreval= txtNombre.get()
    if not nombreval.isalpha():
        txtNombreAdvertencia.config(text="¡Error! Solo se permiten letras.", fg="red")
    else:
        txtNombreAdvertencia.config(text="")


def validar_apellido(event):
    apellidoval= txtApellido.get()
    if not apellidoval.isalpha():
        txtApellidoAdvertencia.config(text="¡Error! Solo se permiten letras.", fg="red")
    else:
        txtApellidoAdvertencia.config(text="")

def validar_edad(event):
    edadval=txtEdad.get()
    if not edadval.isdigit():
        txtEdadAdvertencia.config(text="¡Error! Solo se permiten números.", fg="red")
        return False
    if len(edadval) > 3:
        txtEdadAdvertencia.config(text="¡Error! La edad debe tener como máximo 3 caracteres.", fg="red")
        return False
    else:
        txtCorreoAdvertencia.config(text="")

validacion_edad = ventana.register(validar_edad)

def validar_correo(event):
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@.")
    correoval=txtCorreo.get()
    if not set(correoval).issubset(caracteres_permitidos):
        txtCorreoAdvertencia.config(text="¡Error! Solo se permiten letras, números, @ y punto (.) en el correo electrónico.", fg="red")
        return False
    else:
        txtCorreoAdvertencia.config(text="")
    
validacion_correo = ventana.register(validar_correo)


def validar_fecha(event):
    fechaval=txtFecha.get()
    if len(fechaval) == 2 or len(fechaval)== 5:
        txtFecha.insert(tkinter.END,'/')
    for numero in fechaval:
        if not numero.isdigit() and numero != '/':
            txtFechaAdvertencia.config(text="La fecha de naciemonto debe contener números únicamente",fg="red")
            break

    else:
        txtFechaAdvertencia.config(text="")

    return True

validacion_fecha = ventana.register(validar_fecha)

def insertar_barra(event):
    current_text = txtFecha.get()
    if len(current_text) == 2 or len(current_text) == 5:
        txtFecha.insert(tkinter.END, '/')

labelTitulo= tkinter.Label(ventana, text="Rellene el Formulario")
labelTitulo.grid(column=0, row=0, padx=15, pady=15,columnspan=2)

label1 = tkinter.Label(ventana, text="Nombre")
label1.grid(column=0, row=1, padx=15, pady=15)
txtNombre = tkinter.Entry(ventana, width=20, textvariable=nombre)
txtNombre.grid(column=1, row=1)
txtNombreAdvertencia=tkinter.Label(ventana, text="")
txtNombreAdvertencia.grid(column=0, row=3, columnspan=2)


label2 = tkinter.Label(ventana, text="Apellido")
label2.grid(column=0, row=4, padx=15, pady=15)
txtApellido = tkinter.Entry(ventana, width=20, textvariable=apellido)
txtApellido.grid(column=1, row=4)
txtApellidoAdvertencia=tkinter.Label(ventana, text="")
txtApellidoAdvertencia.grid(column=0, row=5,columnspan=2)

label3 = tkinter.Label(ventana, text="Correo")
label3.grid(column=0, row=6, padx=15, pady=15)
txtCorreo = tkinter.Entry(ventana, width=20, textvariable=correo)
txtCorreo.grid(column=1, row=6)
txtCorreoAdvertencia=tkinter.Label(ventana, text="")
txtCorreoAdvertencia.grid(column=0, row=7,columnspan=2)

label4 = tkinter.Label(ventana, text="Edad")
label4.grid(column=0, row=8, padx=15, pady=15)
txtEdad = tkinter.Entry(ventana, width=20, textvariable=edad)
txtEdad.grid(column=1, row=8)
txtEdadAdvertencia=tkinter.Label(ventana, text="")
txtEdadAdvertencia.grid(column=0, row=9,columnspan=2)

label5 = tkinter.Label(ventana, text="Fecha de Nacimiento")
label5.grid(column=0, row=10, padx=15, pady=15)
txtFecha = tkinter.Entry(ventana, width=20, textvariable=fecha)
txtFecha.grid(column=1, row=10)
txtFechaAdvertencia=tkinter.Label(ventana, text="")
txtFechaAdvertencia.grid(column=0, row=11,columnspan=2)
txtFecha.bind("<KeyRelease>", insertar_barra)

def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseea cerrar la App?"):
        ventana.destroy()

def validar_campos():
    if not (txtNombre.get() and txtApellido.get() and txtCorreo.get() and txtEdad.get() and txtFecha.get()):
        mb.showerror("Error","Debe llenar todos los campos")
    else:
        mb.showinfo("Enhorabuena","Todos los campos han sido validados exitosamente")
    
def limpiarcajas():
    nombre.set("")
    apellido.set("")
    correo.set("")
    edad.set("")
    fecha.set("")
    txtNombre.focus_set()

boton2 = tkinter.Button(ventana, text="Limpiar", command=limpiarcajas)
boton2.grid(column=0, row=12, padx=15, pady=15)

boton3 = tkinter.Button(ventana, text="Validar", command=validar_campos)
boton3.grid(column=0, row=12, padx=15, pady=15, columnspan= 2)

boton1 = tkinter.Button(ventana, text="Salir", command=el_usuario_quiere_salir)
boton1.grid(column=1, row=12, padx=15, pady=15)
txtNombre.bind("<KeyRelease>", validar_nombre)
txtApellido.bind("<KeyRelease>", validar_apellido)
txtEdad.bind("<KeyRelease>", validar_edad)
txtFecha.bind("<KeyRelease>", validar_fecha)
txtCorreo.bind("<KeyRelease>", validar_correo)

ventana.mainloop()
