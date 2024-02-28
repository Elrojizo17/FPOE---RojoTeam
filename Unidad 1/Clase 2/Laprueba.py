from tkinter import Frame, Tk
from tkinter.messagebox import askyesno


Principal = Tk()
Principal.title("Prueba de eventos")

def evento_dar_click(evento):
    frame.focus_set()
    print("Di click e las coordenadas: ", evento.x, evento.y)

def evento_presionar_tecla(evento):
    print("Presione la tecla:", repr(evento.char) )

def el_usuario_quiere_salir( ):
    if askyesno("Salir de la aplicación", "¿Seguro que quieres cerrar la aplicacion?"):
        Principal.destroy()

frame = Frame(Principal, width=500, height=500)
frame.bind("<Button-1>", evento_dar_click)
frame.bind("<Key>", evento_presionar_tecla)
frame.pack()

Principal.protocol("WM_DELETE_WINDOW", el_usuario_quiere_salir)
Principal.mainloop()