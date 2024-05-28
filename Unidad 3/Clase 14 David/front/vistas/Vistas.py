import tkinter
import tkinter.messagebox as messagebox
from Controladores.controladores import Controlador
from Modelos.modelos import Modelos
from vistas.tabla import Tabla

class Vista:
    def __init__(self):
        titulos = ['Identificador', 'Marca', 'Cilindraje', 'Modelo', 'Color']
        columnas = ['id', 'marca', 'cilindraje', 'modelo', 'color']
        data = []
        
        self.ventana = tkinter.Tk()
        self.ventana.title("Moto")
        self.tabla = Tabla(self.ventana, titulos, columnas, data)
        self.controladores = Controlador(self, self.tabla)

        self.ventana.resizable(0, 0)

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

        self.label5 = tkinter.Label(self.ventana, text="Consultar ID")
        self.label5.grid(column=0, row=5, padx=15, pady=15)
        self.txtId = tkinter.Entry(self.ventana, width=20)
        self.txtId.grid(column=1, row=5)

        self.boton1 = tkinter.Button(self.ventana, text="Consultar todo", command=self.controladores.boton_consultar_todo)
        self.boton1.grid(column=0, row=6, padx=15, pady=15)

        self.boton3 = tkinter.Button(self.ventana, text="Guardar", command=lambda: self.controladores.diligenciar())
        self.boton3.grid(column=1, row=6, padx=15, pady=15)

        self.botonConsultar = tkinter.Button(self.ventana, text="Consultar por Id", command=lambda: self.controladores.boton_consultar(self.txtId.get()))
        self.botonConsultar.grid(column=0, row=7, padx=15, pady=15)

        self.botonConsultarTodo = tkinter.Button(self.ventana, text="Actualizar", command=lambda: self.controladores.actualizar(self.txtId.get(), self.txtMarca.get(), self.txtCilindraje.get(), self.txtModelo.get(), self.txtColor.get()))
        self.botonConsultarTodo.grid(column=1, row=7, padx=15, pady=15)

        self.botonFiltrar = tkinter.Button(self.ventana, text="Consultar por Filtro", command=lambda: self.controladores.boton_filtar())
        self.botonFiltrar.grid(column=0, row=8, padx=15, pady=15)

        self.botonActualizar = tkinter.Button(self.ventana, text="Salir", command=self.controladores.el_usuario_quiere_salir)
        self.botonActualizar.grid(column=1, row=8, padx=15, pady=15)

        self.tabla.tabla.grid(column=0, row=9, columnspan=2, padx=15, pady=15)

        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.txtId.delete(0, tkinter.END)
                self.txtId.insert(0, valores[0])
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
                self.controladores.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)
                messagebox.showinfo("Exito", "Papi esa mierda se borro")

                self.txtMarca.delete(0, tkinter.END)
                self.txtCilindraje.delete(0, tkinter.END)
                self.txtModelo.delete(0, tkinter.END)
                self.txtColor.delete(0, tkinter.END)
                self.txtId.delete(0, tkinter.END)
                self.txtMarca.focus_set()
        
        self.controladores.boton_consultar_todo()

        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        self.ventana.mainloop()



