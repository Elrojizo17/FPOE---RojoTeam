import tkinter
from tkinter import messagebox as mb 
from tkinter.messagebox import askyesno

ventana = tkinter.Tk()
ventana.title("Mouse")
ventana.geometry("420x460")
ventana.resizable(0, 0)

marca = tkinter.StringVar()
sensor = tkinter.StringVar()
cantbotones = tkinter.IntVar()
dpi = tkinter.IntVar()



labelTitulo= tkinter.Label(ventana, text="Rellene el Formulario")
labelTitulo.grid(column=0, row=0, padx=15, pady=15,columnspan=2)

label1 = tkinter.Label(ventana, text="Marca")
label1.grid(column=0, row=1, padx=15, pady=15)
txtMarca = tkinter.Entry(ventana, width=20, textvariable=marca)
txtMarca.grid(column=1, row=1)
txtMarcaAdvertencia=tkinter.Label(ventana, text="")
txtMarcaAdvertencia.grid(column=0, row=3, columnspan=2)


label2 = tkinter.Label(ventana, text="Sensor")
label2.grid(column=0, row=4, padx=15, pady=15)
txtSensor = tkinter.Entry(ventana, width=20, textvariable=sensor)
txtSensor.grid(column=1, row=4)
txtSensorAdvertencia=tkinter.Label(ventana, text="")
txtSensorAdvertencia.grid(column=0, row=5,columnspan=2)

label3 = tkinter.Label(ventana, text="Cant. Botones")
label3.grid(column=0, row=6, padx=15, pady=15)
txtBotones = tkinter.Entry(ventana, width=20, textvariable=cantbotones)
txtBotones.grid(column=1, row=6)
txtBotonesAdvertencia=tkinter.Label(ventana, text="")
txtBotonesAdvertencia.grid(column=0, row=7,columnspan=2)

label4 = tkinter.Label(ventana, text="DPI")
label4.grid(column=0, row=8, padx=15, pady=15)
txtDpi = tkinter.Entry(ventana, width=20, textvariable=dpi)
txtDpi.grid(column=1, row=8)
txtDpiAdvertencia=tkinter.Label(ventana, text="")
txtDpiAdvertencia.grid(column=0, row=9,columnspan=2)

def el_usuario_quiere_salir():
    if askyesno("Salir de la Aplicación", "¿Seguro que deseea cerrar la App?"):
        ventana.destroy()

def validar_campos():
    if not (txtMarca.get() and txtSensor.get() and txtBotones.get() and txtDpi.get()):
        mb.showerror("Error","Debe llenar todos los campos")
    else:
        mb.showinfo("Enhorabuena","Todos los campos han sido validados exitosamente")
    
def limpiarcajas():
    marca.set("")
    sensor.set("")
    cantbotones.set("")
    dpi.set("")
    txtMarca.focus_set()

ventana.mainloop()
