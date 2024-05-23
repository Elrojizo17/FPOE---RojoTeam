import tkinter 
import tkinter.messagebox as messagebox
from Controladores.controladores import Controlador
from Modelos.modelos import Modelos

class Vista:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Moto")
        self.ventana.geometry("400x400")
        self.ventana.resizable(0, 0)

        self.controladores = Controlador(self)

        self.label1 = tkinter.Label(self.ventana, text="Marca")
        self.label1.grid(column=0, row=0, padx=15, pady=15)
        self.txtMarca = tkinter.Entry(self.ventana, width=20)
        self.txtMarca.grid(column=1, row=0)

        self.label2 = tkinter.Label(self.ventana, text="cilindraje")
        self.label2.grid(column=0, row=1, padx=15, pady=15)
        self.txtCilindraje = tkinter.Entry(self.ventana, width=20)
        self.txtCilindraje.grid(column=1, row=1)

        self.label3 = tkinter.Label(self.ventana, text="Modelo")
        self.label3.grid(column=0, row=2, padx=15, pady=15)
        self.txtModelo = tkinter.Entry(self.ventana, width=20)
        self.txtModelo.grid(column=1, row=2)

        self.label4 = tkinter.Label(self.ventana, text="Color")
        self.label4.grid(column=0, row=3, padx=15, pady=15)
        self.txtColor = tkinter.Entry(self.ventana, width=20)
        self.txtColor.grid(column=1, row=3)

        self.label5 = tkinter.Label(self.ventana, text="Id")
        self.label5.grid(column=0, row=4, padx=15, pady=15)
        self.txtId = tkinter.Entry(self.ventana, width=20)
        self.txtId.grid(column=1, row=4)

        #self.controladores = Controlador(self)

        '''self.boton2 = tkinter.Button(self.ventana, text="Limpiar", command=self.controladores.limpiarcajas)
        self.boton2.grid(column=0, row=5, padx=15, pady=15)'''

        self.boton1 = tkinter.Button(self.ventana, text="Salir", command=self.controladores.el_usuario_quiere_salir)
        self.boton1.grid(column=1, row=5, padx=15, pady=15)

        self.boton3 = tkinter.Button(self.ventana, text="Validar", command=self.controladores.diligenciar)
        self.boton3.grid(column=3, row=5, padx=15, pady=15)

        self.botonConsultar = tkinter.Button(self.ventana, text="Consultar", command=lambda: self.controladores.boton_consultar(self.txtId.get()))
        self.botonConsultar.grid(column=0, row=6, padx=15, pady=15)

        self.botonConsultarTodo = tkinter.Button(self.ventana, text="Consultar Todo", command=self.controladores.boton_consultar_todo)
        self.botonConsultarTodo.grid(column=1, row=6, padx=15, pady=15)

        self.botonFiltrar = tkinter.Button(self.ventana, text="Filtrar", command=self.controladores.boton_filtar)
        self.botonFiltrar.grid(column=2, row=6, padx=15, pady=15)


        self.ventana.mainloop()


