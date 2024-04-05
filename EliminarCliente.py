import tkinter as tk
from tkinter import *
from tkinter import messagebox
from Tooltip import Tooltip

class EliminarCliente():
   
    def salirSistema(self):
        respuesta = messagebox.askquestion("Salir", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def limpiar(self, event=None):
        self.txtCedula.delete(0, tk.END)
        self.txtNombre.delete(0, tk.END)
        self.txtApellidos.delete(0, tk.END)
        self.txtTelefono.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)

    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe introducir el número de cédula y luego presione el botón buscar, posteriormente presionar el botón eliminar.")
  

    def validarNombre(self, event):
     caracter = event.keysym  # Obtiene el carácter introducido
     if(caracter.isalpha()):  # Verifica si el carácter es una letra - (caracter.isalpha() Valida letras - caracter.isalnum() Valida letras y números)
            self.txtNombre.config(bg="#FFFFFF")  # Cambia el color de fondo del campo de nombre a blanco
     else:
            if(event.keysym != "BackSpace"):  # Verifica si la tecla pulsada no es retroceso
                self.txtNombre.delete(len(self.txtNombre.get())-1, END)  # Borra el último carácter introducido
            
     if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8 and len(self.txtApellidos.get()) >=8 and len(self.txtTelefono.get()) >=10 and len(self.txtEmail.get())>=10):  # Verifica si los campos tienen al menos 8 caracteres
            self.btnEliminar.config(state="normal")  # Habilita el botón de registro
     else:
            self.btnEliminar.config(state="disabled")



    def validarApellidos(self, event):
        caracter = event.keysym  
        if(caracter.isalpha()):  
            self.txtApellidos.config(bg="white") 
        else:
            if(event.keysym != "BackSpace"):  
                self.txtApellidos.delete(len(self.txtNombre.get())-1, END) 
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8 and len(self.txtApellidos.get()) >= 8 and len(self.txtTelefono.get()) >= 10 and len(self.txtEmail.get()) >= 10):  
            self.btnEliminar.config(state="normal")  
        else:
            self.btnEliminar.config(state="disabled")


    def validarCedula(self, event):
       
        caracter = event.keysym  # Obtiene el carácter introducido
        if(caracter.isdigit()):  # Verifica si el carácter es un dígito - (caracter.isdigit() Valida números)
            self.txtCedula.config(bg="#FFFFFF")  # Cambia el color de fondo del campo de cédula a blanco
        else:
            if(event.keysym != "BackSpace"):  # Verifica si la tecla pulsada no es retroceso
                self.txtCedula.delete(len(self.txtCedula.get())-1, END)  # Borra el último carácter introducido
            
        if(len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >= 8 and len(self.txtApellidos.get()) >=8 and len(self.txtTelefono.get()) >=10 and len(self.txtEmail.get())>=10):  # Verifica si los campos tienen al menos 8 caracteres
            self.btnEliminar.config(state="normal")  # Habilita el botón de registro
        else:
            self.btnEliminar.config(state="disabled")
   


    def validarEmail(self, event):
     
        pass

 
    def validarTelefono(self, event):
         caracter = event.keysym  # Obtiene el carácter introducido
         if(caracter.isdigit()):  # Verifica si el carácter es un dígito - (caracter.isdigit() Valida números)
            self.txtTelefono.config(bg="#FFFFFF")  # Cambia el color de fondo del campo de cédula a blanco
         else:
            if(event.keysym != "BackSpace"):  # Verifica si la tecla pulsada no es retroceso
                self.txtTelefono.delete(len(self.txtTelefono.get())-1, END)  # Borra el último carácter introducido
            
         if(len(self.txtTelefono.get()) >= 8 and len(self.txtNombre.get()) >= 8 and len(self.txtCedula.get()) >=8 and len(self.txtTelefono.get()) >=10 and len(self.txtApellidos.get())>=10 and len(self.txtEmail.get())>=10):  # Verifica si los campos tienen al menos 8 caracteres
            self.btnEliminar.config(state="normal")  # Habilita el botón de registro
         else:
            self.btnEliminar.config(state="disabled")
   
      
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(0,0)
        self.ventana.title("Eliminar Cliente")
        self.ventana.config(width=275, height=225)
       

        self.lblTitulo = tk.Label(self.ventana, text="Eliminar Cliente", fg="black")
        self.lblTitulo.place(relx=0.5, rely=0.05, anchor="center")

        self.lblCedula= tk.Label(self.ventana, text="Cédula*", fg="black")
        self.lblCedula.place(relx=0.1, rely=0.12)
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.place(relx=0.3, rely=0.12)
        Tooltip(self.txtCedula, "Ingrese su número de Cédula, mínimo 8 caracteres.\nSolo números [0-9]")
        self.txtCedula.bind('<KeyRelease>', self.validarCedula)
        

        self.lblNombre= tk.Label(self.ventana, text="Nombre*")
        self.lblNombre.place(relx=0.1, rely=0.24)
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.place(relx=0.3, rely=0.24)
        Tooltip(self.txtNombre, "Ingrese su nombre completo, mínimo 8 caracteres.\nSolo letras [a-z]")
        self.txtNombre.bind('<KeyRelease>', self.validarNombre)

        self.lblApellidos= tk.Label(self.ventana, text="Apellidos*")
        self.lblApellidos.place(relx=0.1, rely=0.36)
        self.txtApellidos = tk.Entry(self.ventana)
        self.txtApellidos.place(relx=0.3, rely=0.36)
        Tooltip(self.txtApellidos, "Ingrese sus apellidos.\nSolo recibe letras[a-z]")
        self.txtApellidos.bind('<KeyRelease>', self.validarApellidos)

        self.lblTelefono= tk.Label(self.ventana, text="Teléfono*")
        self.lblTelefono.place(relx=0.1, rely=0.48)
        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.place(relx=0.3, rely=0.48)
        Tooltip(self.txtTelefono, "Ingrese su teléfono.\nSolo recibe números [0-9]")
        self.txtTelefono.bind('<KeyRelease>', self.validarTelefono)
        
        self.lblEmail= tk.Label(self.ventana, text="Email*")
        self.lblEmail.place(relx=0.1, rely=0.60)
        self.txtEmail = tk.Entry(self.ventana)
        self.txtEmail.place(relx=0.3, rely=0.60)
        Tooltip(self.txtEmail, "Ingrese su Correo Electrónico.\nSolo recibe letras, números y los caracteres especiales listados [a-z, 0-9, @, -, _ ]")
        self.txtEmail.bind('<KeyRelease>', self.validarEmail)

        
    
        iconoAyuda = tk.PhotoImage(file= r"icons\icons\help.png")
        self.btnAyuda =tk.Button(self.ventana, image= iconoAyuda)
        self.btnAyuda.place(relx=1, x=-20, y=1, width=25, height=25)
        Tooltip(self.btnAyuda, "Presione para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)  


        
        iconoBuscar = tk.PhotoImage(file= r"icons\icons\magnifier.png")
        self.btnBuscar = tk.Button(self.ventana, text="Buscar", image=iconoBuscar, compound=LEFT)
        self.btnBuscar.place(relx=0.8, rely=0.12)
        Tooltip(self.btnBuscar, "Presione para Buscar la cedula del cliente.\nAlt+b")


        iconoEliminar = tk.PhotoImage(file= r"icons\icons\user_delete.png")
        self.btnEliminar = tk.Button(self.ventana, text="Eliminar", image=iconoEliminar, compound=LEFT)
        self.btnEliminar.place(relx=1, x=-80, rely=1, y=-45, width=60, height=25)
        Tooltip(self.btnEliminar, "Presione este botón para eliminar un cliente.")


        iconoSalir = tk.PhotoImage(file= r"icons\icons\cancel.png")
        self.btnSalir = tk.Button(self.ventana, text="Salir",  image=iconoSalir, compound=LEFT, command=self.salirSistema)
        self.btnSalir.place(x=20, rely=1, y=-45, width=70, height=25)
        Tooltip(self.btnSalir, "Presione para Salir de la Aplicación.\nAlt+s")


        iconoLimpiar = tk.PhotoImage(file= r"icons\icons\textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar",command=self.limpiar, image=iconoLimpiar, compound=LEFT)
        self.btnLimpiar.place(relx=1, x=-170, rely=1, y=-45, width=70, height=25)
        Tooltip(self.btnLimpiar, "Presione para Limpiar los campos de texto.\nAlt+l")

        self.btnAyuda.bind('<Button-1>', self.mostrarAyuda)  
        self.btnSalir.bind('<Button-1>', self.salirSistema)  
        self.btnLimpiar.bind('<Button-1>', self.limpiar)  
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)  
        self.ventana.bind('<Alt-s>', self.salirSistema)
        self.ventana.bind('<Alt-l>', self.limpiar)  
        
    
      

        self.ventana.mainloop()  

app=EliminarCliente()




