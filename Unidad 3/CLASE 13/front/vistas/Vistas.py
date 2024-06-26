
import tkinter
import tkinter.messagebox as messagebox
from Controladores.controladores import Controlador
from Modelos.modelos import Modelos
from .tabla import Tabla

class Vista:
    def __init__(self):
        titulos = ['Identificador', 'Marca', 'Cilindraje', 'Modelo', 'Color']
        columnas = ['id', 'marca', 'cilindraje', 'modelo', 'color']
        data = []
        self.ventana = tkinter.Tk()
        self.ventana.title("Moto")
        self.tabla = Tabla(self.ventana, titulos, columnas, data)
        self.controladores = Controlador(self, self.tabla)

        self.ventana.resizable(0,0)

        self.label1 = tkinter.Label(self.ventana, text="Marca")
        self.label1.grid(column=0, row=0, padx=15, pady=15)
        self.txtMarca = tkinter.Entry(self.ventana, width=20)
        self.txtMarca.grid(column=1, row=0)

        self.label2 = tkinter.Label(self.ventana, text="Cilindraje")
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

        self.labelIdTabla = tkinter.Label(self.ventana, text="Id")
        self.labelIdTabla.grid(column=0, row=4, padx=15, pady=15)
        self.txtIdTabla = tkinter.Entry(self.ventana, width=20)
        self.txtIdTabla.grid(column=1, row=4)

        self.label5 = tkinter.Label(self.ventana, text="Consultar ID")
        self.label5.grid(column=0, row=4, padx=15, pady=15)
        self.txtId = tkinter.Entry(self.ventana, width=20)
        self.txtId.grid(column=1, row=4)

        '''self.boton2 = tkinter.Button(self.ventana, text="Limpiar", command=self.controladores.limpiarcajas)
        self.boton2.grid(column=0, row=5, padx=15, pady=15)'''

        self.boton1 = tkinter.Button(self.ventana, text="Salir", command=self.controladores.el_usuario_quiere_salir)
        self.boton1.grid(column=0, row=5, padx=15, pady=15)

        self.boton3 = tkinter.Button(self.ventana, text="Validar", command=lambda: self.controladores.diligenciar)
        self.boton3.grid(column=1, row=5, padx=15, pady=15)

        self.botonConsultar = tkinter.Button(self.ventana, text="Consultar", command=lambda: self.controladores.boton_consultar(self.txtId.get()))
        self.botonConsultar.grid(column=0, row=6, padx=15, pady=15)

        self.botonConsultarTodo = tkinter.Button(self.ventana, text="Consultar Todo", command=self.controladores.boton_consultar_todo)
        self.botonConsultarTodo.grid(column=1, row=6, padx=15, pady=15)

        self.botonFiltrar = tkinter.Button(self.ventana, text="Filtrar", command=self.controladores.boton_filtar)
        self.botonFiltrar.grid(column=1, row=7, padx=15, pady=15)

        self.botonActualizar = tkinter.Button(self.ventana, text="Actualizar", command=lambda: self.actualizar(self.txtId.get(), self.txtMarca.get(), self.txtCilindraje.get(), self.txtModelo.get(), self.txtColor.get()))
        self.botonActualizar.grid(column=0, row=7, padx=15, pady=15)

        self.tabla.tabla.grid(column=0, row=9, columnspan=2)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.txtIdTabla.delete(0, tkinter.END)
                self.txtIdTabla.insert(0, valores[0])
                self.txtMarca.delete(0, tkinter.END)
                self.txtMarca.insert(0, valores[1])
                self.txtCilindraje.delete(0, tkinter.END)
                self.txtCilindraje.insert(0, valores[2])
                self.txtModelo.delete(0, tkinter.END)
                self.txtModelo.insert(0, valores[3])
                self.txtColor.delete(0, tkinter.END)
                self.txtColor.insert(0, valores[4])

        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<<Delete>>', borrar_elemento)

        self.ventana.mainloop()

    def actualizar(self, id, marca, cilindraje, modelo, color):
        self.controladores.actualizar(id, marca, cilindraje, modelo, color)


