import tkinter as tk 
from tkinter import *
from tkinter import messagebox 
from Tooltip import Tooltip
from CrearCliente import CrearCliente
from EliminarCliente import EliminarCliente
from ModificarCliente import ModificarCliente

class MenuCorresponsal():
    def salirApp(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Coloca el mause sobre el menú cascada, \n esto le permitirá ver todas las opciones del menú.")
  

    def CrearCliente(self):
        registrar = CrearCliente(self.ventana)

    def EliminarCliente(self):
        eliminar = EliminarCliente(self.ventana)

    def ModificarCliente(self):
        generar = ModificarCliente(self.ventana)




    def __init__(self, loggin):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.geometry("550x200")
        self.ventana.focus_set() #Esta función asigna el foco a la ventana secundaria
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)


        self.menu = tk.Menu(self.ventana)#Creamos barra de herramientas y ubicamos en ventana
        self.ventana.config(menu=self.menu)

        menuCliente = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Clientes", menu=menuCliente)
        menuCliente.add_command(label="Registrar Cliente", command=lambda: self.CrearCliente())
        menuCliente.add_separator()
        menuCliente.add_command(label="Eliminar Cliente", command=lambda: self.EliminarCliente())
        menuCliente.add_separator()
        menuCliente.add_command(label="Modificar Cliente", command=lambda: self.ModificarCliente())
        menuCliente.add_separator()

        menuCuentas = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Cuentas", menu=menuCuentas)
        menuCuentas.add_command(label="Crear cuenta", command=lambda: self.CrearCuenta())
        menuCuentas.add_separator()
        menuCuentas.add_command(label="Eliminar cuenta", command=lambda: self.EliminarCuenta())
        menuCuentas.add_separator()

        menuTransacciones = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Transacciones", menu=menuTransacciones) 
        menuTransacciones.add_command(label="Realizar deposito", command=lambda: self.Deposito())
        menuTransacciones.add_separator()
        menuTransacciones.add_command(label="Realizar retiro", command=lambda: self.Retiro())
        menuTransacciones.add_separator()

        menuConsultas = tk.Menu(self.menu)
        self.menu.add_cascade(label="Consultar Información", menu=menuConsultas)
        menuConsultas.add_command(label="Generar Reporte", command=lambda: self.GenerarReporte())
        menuConsultas.add_separator()

        salirMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label= "Salir", menu = salirMenu)
        salirMenu.add_command(label= "Salir", command=lambda: self.salirApp())

        self.lblTitulo = tk.Label(self.ventana, text="Bienvenido al Corresponsal ")
        self.lblTitulo.place(relx=0.5, rely=0.20, anchor="center")

        iconoAyuda = tk.PhotoImage(file= r"icons\help.png")
        self.btnAyuda =tk.Button(self.ventana, image= iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=18, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)

        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

        self.ventana.mainloop()
