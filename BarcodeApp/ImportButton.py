from tkinter import Button, filedialog,ttk
import pandas as pd

class ImportButton:
    def __init__(self, window):
        self.window = window
        
        self.import_button = Button(self.window, text="Importar XLSX", command=self.import_xlsx, font=("Arial", 12),bg="Green",
                                     height=1, width=20, fg="White")
        self.import_button.pack()

    def import_xlsx(self):
        file = filedialog.askopenfilename(filetypes=[("Archivo XLSX", "*.xlsx")])
        if file:
            data = pd.read_excel(file)
            print(data)