from tkinter import Tk
from ImportButton import ImportButton
from tkinter import PhotoImage, Label

class Window:
    def __init__(self):
        self.window = Tk()
        self.icon = PhotoImage(file="bcg.png")
        self.window.geometry("1000x750")
        self.buttton = ImportButton(self.window)
        
    def reSize(event):
        self.width = event.width
        self.height = event.height
        self.label.config(width=self.width // 2, height=self.height // 2, font=("Arial", self.height // 10))

    def execute(self):
        self.window.iconphoto(True,self.icon,self.icon)
        self.window.title("Generador de Bar Code")
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.mainloop()

    def instructions(self):
        self.label = Label(self.window, 
                           text="Para crear los códigos de barras, debes subir un archivo .xlsx en el cual en la primera columna estén todos los códigos a ejecutar, posteriormente deberás seleccionar el formato.",font=("Arial", 12), background="green", foreground="white")
        self.label.pack(padx=10, pady=10)