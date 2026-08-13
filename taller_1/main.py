import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

class ArrayInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Arrays - Taller 1")
        self.root.geometry("1200x900")
        self.root.configure(bg="#f0f0f0")
        
        # Arrays
        self.array1 = []
        self.array2d = [[], [], []]
        
        # Variables para mostrar en las pestañas
        self.array1_display = None
        self.array2d_display = None
        
        # Crear notebook (pestañas)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Pestaña 1: Entrada de arrays
        self.create_tab1()
        
        # Pestaña 2: Acceso a elementos
        self.create_tab2()
        
        # Pestaña 3: Insertar y eliminar
        self.create_tab3()
        
        # Pestaña 4: Búsqueda de índices
        self.create_tab4()
    
    def update_display_tab1(self, array1_display, array2d_display):
        """Actualiza los displays de la pestaña 1"""
        array1_display.config(state="normal")
        array1_display.delete(1.0, tk.END)
        array1_display.insert(tk.END, f"array1 = {self.array1}")
        array1_display.config(state="disabled")
        
        array2d_display.config(state="normal")
        array2d_display.delete(1.0, tk.END)
        array2d_display.insert(tk.END, "array2d = [\n")
        for i, row in enumerate(self.array2d):
            array2d_display.insert(tk.END, f"  {row}")
            if i < 2:
                array2d_display.insert(tk.END, ",\n")
        array2d_display.insert(tk.END, "\n]")
        array2d_display.config(state="disabled")
    
    def update_display_tab3(self, array1_result, array2d_result):
        """Actualiza los displays de la pestaña 3"""
        array1_result.config(state="normal")
        array1_result.delete(1.0, tk.END)
        array1_result.insert(tk.END, f"array1 = {self.array1}")
        array1_result.config(state="disabled")
        
        array2d_result.config(state="normal")
        array2d_result.delete(1.0, tk.END)
        array2d_result.insert(tk.END, "array2d = [\n")
        for i, row in enumerate(self.array2d):
            array2d_result.insert(tk.END, f"  {row}")
            if i < 2:
                array2d_result.insert(tk.END, ",\n")
        array2d_result.insert(tk.END, "\n]")
        array2d_result.config(state="disabled")
    
    def create_tab1(self):
        """Primera parte: Entrada de arrays"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Parte 1: Ingresar Arrays")
        
        # Título
        title = tk.Label(frame, text="Parte 1: Ingresar Elementos en los Arrays", 
                        font=("Arial", 14, "bold"), bg="#e8f4f8")
        title.pack(fill="x", padx=10, pady=10)
        
        # Sección Array 1D
        array1_frame = ttk.LabelFrame(frame, text="Array 1D (5 elementos)")
        array1_frame.pack(fill="x", padx=10, pady=10)
        
        array1_input = tk.Entry(array1_frame, width=30, font=("Arial", 10))
        array1_input.pack(side="left", padx=5, pady=5)
        array1_input.insert(0, "Ingresa elemento")
        
        # Display de Array 1D
        array1_display = scrolledtext.ScrolledText(array1_frame, height=3, width=80, 
                                                   state="disabled", font=("Courier", 10))
        array1_display.pack(fill="x", padx=5, pady=5)
        
        def add_array1():
            value = array1_input.get().strip()
            if value and value != "Ingresa elemento" and len(self.array1) < 5:
                self.array1.append(value)
                self.update_display_tab1(array1_display, array2d_display)
                array1_input.delete(0, tk.END)
                array1_input.insert(0, "Ingresa elemento")
                messagebox.showinfo("Éxito", f"'{value}' añadido (Total: {len(self.array1)}/5)")
            elif len(self.array1) >= 5:
                messagebox.showwarning("Lleno", "El array 1D ya tiene 5 elementos")
        
        tk.Button(array1_frame, text="Agregar", command=add_array1, 
                 bg="#4CAF50", fg="white").pack(side="left", padx=5, pady=5)
        
        # Sección Array 2D
        array2d_frame = ttk.LabelFrame(frame, text="Array 2D (3x3)")
        array2d_frame.pack(fill="x", padx=10, pady=10)
        
        # Selección de fila
        tk.Label(array2d_frame, text="Fila:").pack(side="left", padx=5, pady=5)
        row_spin = tk.Spinbox(array2d_frame, from_=0, to=2, width=3, font=("Arial", 10))
        row_spin.delete(0, tk.END)
        row_spin.insert(0, "0")
        row_spin.pack(side="left", padx=5, pady=5)
        
        tk.Label(array2d_frame, text="Elemento:").pack(side="left", padx=5, pady=5)
        array2d_input = tk.Entry(array2d_frame, width=20, font=("Arial", 10))
        array2d_input.pack(side="left", padx=5, pady=5)
        array2d_input.insert(0, "Ingresa elemento")
        
        def add_array2d():
            try:
                row = int(row_spin.get())
                value = array2d_input.get().strip()
                if value and value != "Ingresa elemento" and len(self.array2d[row]) < 3:
                    self.array2d[row].append(value)
                    self.update_display_tab1(array1_display, array2d_display)
                    array2d_input.delete(0, tk.END)
                    array2d_input.insert(0, "Ingresa elemento")
                    total = sum(len(r) for r in self.array2d)
                    messagebox.showinfo("Éxito", f"'{value}' añadido a fila {row} (Total: {total}/9)")
                elif len(self.array2d[row]) >= 3:
                    messagebox.showwarning("Lleno", f"La fila {row} ya tiene 3 elementos")
            except:
                messagebox.showerror("Error", "Fila inválida")
        
        tk.Button(array2d_frame, text="Agregar", command=add_array2d, 
                 bg="#2196F3", fg="white").pack(side="left", padx=5, pady=5)
        
        # Display de Array 2D
        array2d_display = scrolledtext.ScrolledText(array2d_frame, height=4, width=80, 
                                                    state="disabled", font=("Courier", 10))
        array2d_display.pack(fill="x", padx=5, pady=5)
        
        # Botón para limpiar
        def clear_all():
            self.array1 = []
            self.array2d = [[], [], []]
            self.update_display_tab1(array1_display, array2d_display)
            messagebox.showinfo("Limpios", "Arrays limpiados")
        
        tk.Button(frame, text="Limpiar Arrays", command=clear_all, 
                 bg="#FF9800", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
        
        self.update_display_tab1(array1_display, array2d_display)
    
    def create_tab2(self):
        """Segunda parte: Acceso a elementos específicos"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Parte 2: Acceso a Elementos")
        
        title = tk.Label(frame, text="Parte 2: Mostrar Elementos Específicos", 
                        font=("Arial", 14, "bold"), bg="#f3e5f5")
        title.pack(fill="x", padx=10, pady=10)
        
        # Acceso a array1[1]
        array1_frame = ttk.LabelFrame(frame, text="array1[1]")
        array1_frame.pack(fill="x", padx=10, pady=10)
        
        array1_label = tk.Label(array1_frame, text="", font=("Arial", 12, "bold"), 
                               fg="#1976D2", bg="#E3F2FD", padx=20, pady=15)
        array1_label.pack(fill="x", padx=10, pady=10)
        
        tk.Label(array1_frame, text="Código: print(array1[1])", 
                font=("Arial", 10, "italic")).pack(anchor="w", padx=20, pady=5)
        
        # Acceso a array2d[1][1]
        array2d_frame = ttk.LabelFrame(frame, text="array2d[1][1]")
        array2d_frame.pack(fill="x", padx=10, pady=10)
        
        array2d_label = tk.Label(array2d_frame, text="", font=("Arial", 12, "bold"), 
                                fg="#C2185B", bg="#FCE4EC", padx=20, pady=15)
        array2d_label.pack(fill="x", padx=10, pady=10)
        
        tk.Label(array2d_frame, text="Código: print(array2d[1][1])", 
                font=("Arial", 10, "italic")).pack(anchor="w", padx=20, pady=5)
        
        def update_values():
            try:
                valor1 = self.array1[1] if len(self.array1) > 1 else "Índice fuera de rango"
                array1_label.config(text=f"Resultado: '{valor1}'")
            except IndexError:
                array1_label.config(text="Error: Índice fuera de rango")
            
            try:
                valor2 = self.array2d[1][1] if len(self.array2d[1]) > 1 else "Índice fuera de rango"
                array2d_label.config(text=f"Resultado: '{valor2}'")
            except IndexError:
                array2d_label.config(text="Error: Índice fuera de rango")
        
        # Botón para refrescar
        tk.Button(frame, text="Actualizar Valores", command=update_values, 
                 bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).pack(pady=15)
        
        update_values()
    
    def create_tab3(self):
        """Tercera parte: Insertar y eliminar"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Parte 3: Insert y Pop")
        
        title = tk.Label(frame, text="Parte 3: Modificar Arrays (Insert y Pop)", 
                        font=("Arial", 14, "bold"), bg="#e8f5e9")
        title.pack(fill="x", padx=10, pady=10)
        
        # Insert en Array 1D
        insert_frame = ttk.LabelFrame(frame, text="Insert: array1.insert(2, 'Estructura de datos')")
        insert_frame.pack(fill="x", padx=10, pady=10)
        
        insert_input = tk.Entry(insert_frame, width=30, font=("Arial", 10))
        insert_input.pack(side="left", padx=5, pady=5)
        insert_input.insert(0, "Estructura de datos")
        
        array1_result = scrolledtext.ScrolledText(insert_frame, height=3, width=80, 
                                                 state="disabled", font=("Courier", 10))
        array1_result.pack(fill="x", padx=5, pady=5)
        
        # Pop en Array 2D
        pop_frame = ttk.LabelFrame(frame, text="Pop: array2d[2].pop(2)")
        pop_frame.pack(fill="x", padx=10, pady=10)
        
        array2d_result = scrolledtext.ScrolledText(pop_frame, height=4, width=80, 
                                                  state="disabled", font=("Courier", 10))
        array2d_result.pack(fill="x", padx=5, pady=5)
        
        def do_insert():
            value = insert_input.get().strip()
            if value:
                self.array1.insert(2, value)
                self.update_display_tab3(array1_result, array2d_result)
                messagebox.showinfo("Éxito", f"'{value}' insertado en posición 2")
        
        tk.Button(insert_frame, text="Insertar en pos 2", command=do_insert, 
                 bg="#4CAF50", fg="white").pack(side="left", padx=5, pady=5)
        
        def do_pop():
            try:
                if len(self.array2d[2]) > 2:
                    removed = self.array2d[2].pop(2)
                    self.update_display_tab3(array1_result, array2d_result)
                    messagebox.showinfo("Éxito", f"'{removed}' eliminado de array2d[2][2]")
                else:
                    messagebox.showwarning("Error", "No hay elemento en array2d[2][2]")
            except:
                messagebox.showerror("Error", "Error al eliminar")
        
        tk.Button(pop_frame, text="Eliminar array2d[2][2]", command=do_pop, 
                 bg="#f44336", fg="white").pack(side="left", padx=5, pady=5)
        
        self.update_display_tab3(array1_result, array2d_result)
    
    def create_tab4(self):
        """Cuarta parte: Búsqueda de índices"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Parte 4: Index (Búsqueda)")
        
        title = tk.Label(frame, text="Parte 4: Búsqueda de Índices (.index())", 
                        font=("Arial", 14, "bold"), bg="#fce4ec")
        title.pack(fill="x", padx=10, pady=10)
        
        # Buscar en Array 1D
        array1_frame = ttk.LabelFrame(frame, text="Buscar en array1")
        array1_frame.pack(fill="x", padx=10, pady=10)
        
        array1_search = tk.Entry(array1_frame, width=30, font=("Arial", 10))
        array1_search.pack(side="left", padx=5, pady=5)
        array1_search.insert(0, "Estructura de datos")
        
        array1_result = tk.Label(array1_frame, text="", font=("Arial", 12, "bold"), 
                                fg="#1976D2", bg="#E3F2FD")
        array1_result.pack(fill="x", padx=5, pady=5)
        
        array1_search_status = scrolledtext.ScrolledText(array1_frame, height=3, width=80, 
                                                        state="disabled", font=("Courier", 10))
        array1_search_status.pack(fill="x", padx=5, pady=5)
        
        def search_array1():
            value = array1_search.get().strip()
            try:
                index = self.array1.index(value)
                array1_result.config(text=f"✓ Encontrado: array1.index('{value}') = {index}")
                array1_search_status.config(state="normal")
                array1_search_status.delete(1.0, tk.END)
                array1_search_status.insert(tk.END, f"array1 = {self.array1}\nÍndice de '{value}': {index}")
                array1_search_status.config(state="disabled")
            except ValueError:
                array1_result.config(text=f"✗ No encontrado: '{value}' no está en array1")
                array1_search_status.config(state="normal")
                array1_search_status.delete(1.0, tk.END)
                array1_search_status.insert(tk.END, f"array1 = {self.array1}\nError: '{value}' no existe")
                array1_search_status.config(state="disabled")
        
        tk.Button(array1_frame, text="Buscar", command=search_array1, 
                 bg="#4CAF50", fg="white").pack(side="left", padx=5, pady=5)
        
        # Buscar en Array 2D (fila 1)
        array2d_frame = ttk.LabelFrame(frame, text="Buscar en array2d fila 1")
        array2d_frame.pack(fill="x", padx=10, pady=10)
        
        array2d_search = tk.Entry(array2d_frame, width=30, font=("Arial", 10))
        array2d_search.pack(side="left", padx=5, pady=5)
        array2d_search.insert(0, "Busca un elemento")
        
        array2d_result = tk.Label(array2d_frame, text="", font=("Arial", 12, "bold"), 
                                 fg="#C2185B", bg="#FCE4EC")
        array2d_result.pack(fill="x", padx=5, pady=5)
        
        array2d_search_status = scrolledtext.ScrolledText(array2d_frame, height=3, width=80, 
                                                         state="disabled", font=("Courier", 10))
        array2d_search_status.pack(fill="x", padx=5, pady=5)
        
        def search_array2d():
            value = array2d_search.get().strip()
            try:
                if value in self.array2d[1]:
                    col_idx = self.array2d[1].index(value)
                    array2d_result.config(text=f"✓ Encontrado: array2d[1].index('{value}') = {col_idx}")
                    array2d_search_status.config(state="normal")
                    array2d_search_status.delete(1.0, tk.END)
                    array2d_search_status.insert(tk.END, f"array2d[1] = {self.array2d[1]}\nÍndice de '{value}': {col_idx}")
                    array2d_search_status.config(state="disabled")
                else:
                    raise ValueError(f"'{value}' no encontrado")
            except ValueError:
                array2d_result.config(text=f"✗ No encontrado: '{value}' no está en array2d fila 1")
                array2d_search_status.config(state="normal")
                array2d_search_status.delete(1.0, tk.END)
                array2d_search_status.insert(tk.END, f"array2d[1] = {self.array2d[1]}\nError: '{value}' no existe")
                array2d_search_status.config(state="disabled")
        
        tk.Button(array2d_frame, text="Buscar en fila 1", command=search_array2d, 
                 bg="#2196F3", fg="white").pack(side="left", padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayInterface(root)
    root.mainloop()
