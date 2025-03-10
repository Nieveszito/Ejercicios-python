import tkinter as tk
from ejercicios import Ejercicio1, Ejercicio2, Ejercicio3, Ejercicio4, Ejercicio5, Ejercicio6, Ejercicio7, Ejercicio8, Ejercicio9, Ejercicio10

# Clase principal para gestionar la interfaz
class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú de Ejercicios")
        
        # Cambiar el color de fondo de la ventana principal
        self.root.config(bg='lightblue')  
        
        self.frame = None
        self.mostrar_menu()
    
    def mostrar_menu(self):
        if self.frame:
            self.frame.destroy()
        
        # Crear un frame con un fondo específico
        self.frame = tk.Frame(self.root, bg='lightgreen')
        self.frame.pack(fill="both", expand=True)
        
        # Etiquetas con fondo personalizado
        tk.Label(self.frame, text="NIEVES SANDOVAL ROBERTO GAEL", bg='lightgreen').pack(pady=10)
        tk.Label(self.frame, text="Selecciona un ejercicio", bg='lightgreen').pack(pady=10)
        
        # Botones con fondo personalizado
        ejercicios = [Ejercicio1, Ejercicio2, Ejercicio3, Ejercicio4, Ejercicio5, Ejercicio6, Ejercicio7, Ejercicio8, Ejercicio9, Ejercicio10]  # Agrega más ejercicios según los vayas implementando
        for i, ejercicio in enumerate(ejercicios, 1):
            tk.Button(self.frame, text=f"Ejercicio {i}", command=lambda e=ejercicio: self.mostrar_ejercicio(e)).pack(pady=5)
    
    def mostrar_ejercicio(self, clase):
        if self.frame:
            self.frame.destroy()
        
        # Crear un nuevo frame para el ejercicio con fondo diferente
        self.frame = tk.Frame(self.root, bg='lightyellow')
        self.frame.pack(fill="both", expand=True)
        
        # Crear el ejercicio en el nuevo frame
        clase(self.frame, self.mostrar_menu)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()
