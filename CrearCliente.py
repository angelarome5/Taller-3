import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class CrearCliente():
    def salirSistema(self):
        respuesta = messagebox.askquestion("Salir", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def limpiar(self):
        self.txtCedula.delete(0, tk.END)
        self.txtNombre.delete(0, tk.END)
        self.txtApellidos.delete(0, tk.END)
        self.txtTelefono.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)


    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe diligenciar todos los campos marcados con *, luego presione el botón crear.")

    def validarCedula(self, event):
        caracter = event.keysym 
        if(caracter.isdigit()): 
            self.txtCedula.config(bg="#FFFFFF")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtCedula.delete(len(self.txtCedula.get())-1, END) 
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8): 
            self.btnAgregar.config(state="normal") 
        else:
            self.btnAgregar.config(state="disabled")  


    def validarNombre(self, event): 
        caracter = event.keysym  
        if(caracter.isalpha()): 
            self.txtNombre.config(bg="#FFFFFF")  
        else:
            if(event.keysym != "BackSpace"): 
                self.txtNombre.delete(len(self.txtNombre.get())-1, END) 
            
            

    def validarApellido(self, event):
        caracter = event.keysym  
        if(caracter.isalpha()):  
            self.txtApellidos.config(bg="#FFFFFF")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtApellidos.delete(len(self.txtApellidos.get())-1, END) 
            
    
    def validarTelefono(self, event):
        caracter = event.keysym  
        if(caracter.isdigit()):  
            self.txtTelefono.config(bg="#FFFFFF")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtTelefono.delete(len(self.txtTelefono.get())-1, END) 
       

    def validarEmail(self, event):
        caracter = event.keysym  
        if(caracter.isalnum()):   
            self.txtEmail.config(bg="#FFFFFF")  
        else:
            if(event.keysym != "BackSpace"):  
                self.txtEmail.delete(len(self.txtEmail.get())-1, END) 

        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8 and len(self.txtApellidos.get()) >= 8 and len(self.txtTelefono()) >= 8 and len(self.txtEmail()) >= 8): 
            self.btnAgregar.config(state="normal") 
        else:
            self.btnAgregar.config(state="disabled")  
       

           
    def __init__(self, MenuCorresponsal):
        self.ventana = tk.Toplevel(MenuCorresponsal)
        self.ventana.title("Crear Cliente")
        self.ventana.resizable(0,0)
        self.ventana.config(width=275, height=225)
    

        self.lblTitulo = tk.Label(self.ventana, text="Crear Cliente", fg="black")
        self.lblTitulo.place(relx=0.5, rely=0.05, anchor="center")
        self.lblCedula= tk.Label(self.ventana, text="Cédula*", fg="black")
        self.lblCedula.place(relx=0.1, rely=0.10)
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=0.3, rely=0.10)
        Tooltip(self.txtCedula, "Ingrese su número de Cédula, mínimo 8 caracteres.\nSolo números [0-9]")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)

        self.lblNombre= tk.Label(self.ventana, text="Nombre*")
        self.lblNombre.place(relx=0.1, rely=0.22)
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx=0.3, rely=0.22)
        Tooltip(self.txtNombre, "Ingrese su nombre completo, mínimo 8 caracteres.\nSolo letras [a-z]")
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)

        self.lblApellidos= tk.Label(self.ventana, text="Apellidos*")
        self.lblApellidos.place(relx=0.1, rely=0.34)
        self.txtApellidos = tk.Entry(self.ventana)
        self.txtApellidos.place(relx=0.3, rely=0.34)
        Tooltip(self.txtApellidos, "Ingrese su apellido completo, mínimo 8 caracteres.\nSolo letras [a-z]")
        self.txtApellidos.bind('<KeyRelease>', self.validarApellido)

        self.lblTelefono= tk.Label(self.ventana, text="Teléfono*")
        self.lblTelefono.place(relx=0.1, rely=0.46)
        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(relx=0.3, rely=0.46)
        Tooltip(self.txtTelefono, "Ingrese su número de telefono.\nSolo números [0-9]")
        self.txtTelefono.bind('<KeyRelease>', self.validarTelefono)


        self.lblEmail= tk.Label(self.ventana, text="Email*")
        self.lblEmail.place(relx=0.1, rely=0.58)
        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.3, rely=0.58)
        Tooltip(self.txtEmail, "Ingrese su email.")
        self.txtEmail.bind('<KeyRelease>', self.validarEmail)

        iconoAgregar = tk.PhotoImage(file= r"C:\Users\ASUS\Downloads\Taller 3\Taller3\Taller-3\icons\icons\add.png")
        self.btnAgregar = tk.Button(self.ventana, image=iconoAgregar, compound=LEFT,  text="Crear" )
        self.btnAgregar.place(relx=0.1, rely=0.70)
    
        iconoLimpiar = tk.PhotoImage(file= r"C:\Users\ASUS\Downloads\Taller 3\Taller3\Taller-3\icons\icons\delete.png")
        self.btnLimpiar = tk.Button(self.ventana, image=iconoLimpiar, text="Limpiar", compound=LEFT, command=self.limpiar)
        self.btnLimpiar.place(relx=0.4, rely=0.70)
        iconoSalir = tk.PhotoImage(file= r"C:\Users\ASUS\Downloads\Taller 3\Taller3\Taller-3\icons\icons\cancel.png")
        self.btnSalir = tk.Button(self.ventana,  image=iconoSalir, compound=LEFT, text="Salir", command=lambda: self.salirSistema() )
        self.btnSalir.place(relx=0.7, rely=0.70)

        iconoAyuda = tk.PhotoImage(file= r"C:\Users\ASUS\Downloads\Taller 3\Taller3\Taller-3\icons\icons\help.png")
        self.btnAyuda =tk.Button(self.ventana, image= iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=25, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)

        self.ventana.bind('<Alt-a>', self.mostrarAyuda)
        
        self.ventana.mainloop()


