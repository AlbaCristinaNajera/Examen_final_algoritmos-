import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from examen import crear_vehiculo
import sys

class InterfazGrafica: 
    #Inicializamos como vacios lso elementos de GUI 
    etiqueta_codigo = None 
    codigo_entry=None
    etiqueta_marca = None 
    marca_entry = None 
    etiqueta_modelo = None 
    modelo_entry = None 
    etiqueta_precio = None 
    precio_entry = None
    etiqueta_kilometraje = None 
    kilometraje_entry = None
    boton_guardar = None 
    boton_editar = None
    boton_eliminar = None 
    boton_listar = None 

    def guardar_vehiculos_clik():

    #Constructor, se ejecutara al crear una instancia de la clase InterfazGrafica
    #con la etiqueta self se obtienen los valores 
        def crear_vehiculo(self):
            crear_vehiculo(self.codigo_entry.get(),self.marca_entry.get(),self.modelo_entry.get(),self.precio_entry.get(),self.kilometraje_entry.get())
            messagebox.showinfo(message="Vehículo creado con éxito", title= "Titulo")
        def __init__(self):
            
            print("Abriendo ventana Interfaz")
            ventana = tk.Tk()
            ventana.title("Crear Vehículo")
            ventana.config(width=400, height=300)
            self.etiqueta_codigo= ttk.Label(text="Escriba el codigo")
            self.codigo_entry= ttk.Entry()
            self.etiqueta_marca= ttk.Label(text="Ingrese la marca")
            self.marca_entry = ttk.Entry()
            self.etiqueta_modelo= ttk.Label(text="Ingrese el modelo")
            self.modelo_entry = ttk.Entry()
            self.etiqueta_precio= ttk.Label(text="Ingrese el precio")
            self.precio_entry = ttk.Entry()
            self.etiqueta_kilometraje= ttk.Label(text="Ingrese el kilometraje")
            self.kilometraje_entry = ttk.Entry()
            self.etiqueta_codigo.place(x=20, y=20)
            self.codigo_entry.place(x=20, y=40, width=200)
            self.etiqueta_marca.place(x=20, y=65)
            self.marca_entry.place(x=20, y=85, width=200)
            self.etiqueta_modelo.place(x=20, y=110)
            self.modelo_entry.place(x=20, y=130, width=200)
            self.etiqueta_precio.place(x=20, y=110)
            self.precio_entry.place(x=20, y=150, width=200)
            self.etiqueta_kilometraje.place(x=20, y=110)
            self.kilometraje_entry.place(x=20, y=175, width=200)
            self.boton_guardar= ttk.Button(text="Guardar los datos", command=getattr(self, "guardar_vehiculos_click"))
            self.boton_enviar.place(x=20, y=190)
            ventana.mainloop()

interfaz = InterfazGrafica()




