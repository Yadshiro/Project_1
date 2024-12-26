# Ejemplo en una aplicación GUI (Python con Tkinter)
import tkinter as tk

def run_simulation():
    # Función para ejecutar la simulación
    pass

root = tk.Tk()
toolbar = tk.Frame(root, bg="gray")

run_button = tk.Button(toolbar, text="Iniciar simulación", command=run_simulation)
run_button.pack(side="left", padx=2, pady=2)

toolbar.pack(side="top", fill="x")
root.mainloop()

from tkinter import filedialog

def load_inp_file():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos INP", "*.inp")])
    if file_path:
        # Añade aquí la lógica para crear y visualizar las capas de formas
        pass

load_button = tk.Button(toolbar, text="Cargar archivo INP", command=load_inp_file)
load_button.pack(side="left", padx=2, pady=2)

