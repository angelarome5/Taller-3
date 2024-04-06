import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class ModificarCliente():
    def salirSistema(self, event):
        respuesta = messagebox.askquestion("Salir", "Está seguro de que quiere salir de la Aplicación?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def limpiar(self, event):
        self.txtCedula.delete(0, END)
        self.txtNombre.delete(0, END)
        self.txtApellidos.delete(0, END)
        self.txtTelefono.delete(0, END)
        self.txtEmail.delete(0, END)
        self.btnBuscar.config(state = "disabled")
        self.txtCedula.focus_set()

    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe introducir el número de cédula, luego presionar el botón buscar, posteriormente digite el dato que desea cambiar y presione el botón modificar.")

    def validarCedula(self, event):
        numero = event.keysym  
        if(numero.isdigit()):
            self.txtCedula.config(bg="white")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtCedula.delete(len(self.txtCedula.get())-1, END)  
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8):  
            self.btnBuscar.config(state="normal")  
        else:
            self.btnBuscar.config(state="disabled")

    def validarNombre(self, event):
        caracter = event.keysym  
        if(caracter.isalpha()):  
            self.txtNombre.config(bg="white") 
        else:
            if(event.keysym != "BackSpace"):  
                self.txtNombre.delete(len(self.txtNombre.get())-1, END) 
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8 and len(self.txtApellidos.get()) >= 8 and len(self.txtTelefono.get()) >= 10 and len(self.txtEmail.get()) >= 10):  
            self.btnModificar.config(state="normal")  
        else:
            self.btnModificar.config(state="disabled")  

    def validarApellidos(self, event):
        caracter = event.keysym  
        if(caracter.isalpha()):  
            self.txtApellidos.config(bg="white") 
        else:
            if(event.keysym != "BackSpace"):  
                self.txtApellidos.delete(len(self.txtNombre.get())-1, END) 
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8 and len(self.txtApellidos.get()) >= 8 and len(self.txtTelefono.get()) >= 10 and len(self.txtEmail.get()) >= 10):  
            self.btnModificar.config(state="normal")  
        else:
            self.btnModificar.config(state="disabled") 

    def validarEmail(self, event):
        return True  
    
    def validarTelefono(self, event):
        caracter = event.keysym  
        if(caracter.isdigit()):  
            self.txtTelefono.config(bg="White")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtTelefono.delete(len(self.txtTelefono.get())-1, END)  
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8 and len(self.txtApellidos.get()) >= 8 and len(self.txtTelefono.get()) >= 10 and len(self.txtEmail.get()) >= 10):
            self.btnModificar.config(state="normal")  
        else:
            self.btnModificar.config(state="disabled")
    
    def __init__(self, MenuCorresponsal):
        self.ventana = tk.Toplevel(MenuCorresponsal)
        self.ventana.resizable(0,0)
        self.ventana.title("Modificar Cliente")
        self.ventana.config(width=275, height=225)

        self.lblTitulo = tk.Label(self.ventana, text="Modificar Cliente", fg="black")
        self.lblTitulo.place(relx=0.5, rely=0.05, anchor="center")

        self.lblCedula= tk.Label(self.ventana, text="Cédula*", fg="black")
        self.lblCedula.place(relx=0.1, rely=0.12)
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=0.3, rely=0.12)
        Tooltip(self.txtCedula, "Ingrese su número de cédula, minimo 10 caracteres.\nSolo números [0-9]")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)

        self.lblNombre= tk.Label(self.ventana, text="Nombre*")
        self.lblNombre.place(relx=0.1, rely=0.24)
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx=0.3, rely=0.24)
        Tooltip(self.txtNombre, "Ingrese su nombre, minimo 10 caracteres. \nSolo letras [a-z]") 
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)

        self.lblApellidos= tk.Label(self.ventana, text="Apellidos*")
        self.lblApellidos.place(relx=0.1, rely=0.36)
        self.txtApellidos = tk.Entry(self.ventana)
        self.txtApellidos.place(relx=0.3, rely=0.36)
        Tooltip(self.txtApellidos, "Ingrese su apellido, minimo 10 caracteres. \nSolo letras [a-z]") 
        self.txtApellidos.bind('<KeyRelease>', self.validarApellidos)

        self.lblTelefono= tk.Label(self.ventana, text="Teléfono*")
        self.lblTelefono.place(relx=0.1, rely=0.48)
        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(relx=0.3, rely=0.48)
        Tooltip(self.txtTelefono, "Ingrese su número de teléfono, mínimo 10 caracteres.\nSolo números [0-9]")
        self.txtTelefono.bind('<KeyRelease>', self.validarTelefono)

        self.lblEmail= tk.Label(self.ventana, text="Email*")
        self.lblEmail.place(relx=0.1, rely=0.60)
        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.3, rely=0.60)
        Tooltip(self.txtEmail, "Ingrese su Correo Electrónico.\nSolo recibe letras, números y los caracteres especiales listados [a-z, 0-9, @, -, _ ]")
        self.txtEmail.bind('<KeyRelease>', self.validarEmail)

        iconoBuscar = tk.PhotoImage(file= r"icons\magnifier.png")
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", image=iconoBuscar, compound=LEFT)
        self.btnBuscar.place(relx=0.8, rely=0.12)
        Tooltip(self.btnBuscar, "Presione para Buscar la cedula del cliente.\nAlt+b")

        iconoSalir = tk.PhotoImage(file= r"icons\cancel.png")
        self.btnSalir = tk.Button(self.ventana, text="Salir", image=iconoSalir, compound=LEFT)
        self.btnSalir.place(relx=1, x=-80, rely=1, y=-45, width=60, height=25)
        Tooltip(self.btnSalir, "Presione para Salir de la Aplicación.\nAlt+s")

        iconoModificar = tk.PhotoImage(file=r"icons\layout_edit.png")
        self.btnModificar = tk.Button(self.ventana, text="Modificar", image=iconoModificar, compound=LEFT, state="disabled", command=lambda:self.modificarUsuario())
        self.btnModificar.place(x=20, rely=1, y=-45, width=75, height=25)
        Tooltip(self.btnModificar, "Presione para modificar el cliente o presione la tecla Enter.\n")

        iconoLimpiar = tk.PhotoImage(file= r"icons\textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar", image=iconoLimpiar, compound=LEFT)
        self.btnLimpiar.place(relx=1, x=-170, rely=1, y=-45, width=70, height=25)
        Tooltip(self.btnLimpiar, "Presione para Limpiar los campos de texto.\nAlt+l")

        iconoAyuda = tk.PhotoImage(file= r"icons\help.png")
        self.btnAyuda =tk.Button(self.ventana, image= iconoAyuda)
        self.btnAyuda.place(relx=1, x=-20, y=1, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)

        self.ventana.bind('<Alt-a>', self.mostrarAyuda)
        
        self.ventana.mainloop()


