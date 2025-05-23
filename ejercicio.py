import tkinter as tk
from tkinter import messagebox

# Lista global para almacenar los artículos
articulos = []

# Función para eliminar un artículo seleccionado
def eliminar_articulo():
    seleccion = lista_articulos.curselection()
    if seleccion:
        index = seleccion[0]
        del articulos[index]
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "Debes seleccionar un artículo para eliminar")


# Función para agregar un nuevo artículo
def agregar_articulo():
    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    # Agregar el artículo a la lista
    articulos.append({"codigo": codigo, "nombre": nombre, "precio": float(precio)})
    actualizar_lista()
    # Limpiar los campos
    entry_codigo.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
# Función para actualizar la lista en la interfaz
def actualizar_lista():
    lista_articulos.delete(0, tk.END) # Limpiar la lista
    for articulo in articulos:
        lista_articulos.insert(tk.END, f"{articulo['codigo']} - {articulo['nombre']} - {articulo['precio']:,.2f}")

# Función para cerrar la ventana
def cerrar():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Mi primera aplicación")
# Definir el tamaño de la ventana
root.geometry("800x600")

tk.Label(root, text="Numero de jugador:").grid(row=0, column=0, padx=10, pady=5)
entry_codigo = tk.Entry(root)
entry_codigo.grid(row=0, column=1)
tk.Label(root, text="Nombre del jugador:").grid(row=1, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=1, column=1)
tk.Label(root, text="Precio del contrato:").grid(row=2, column=0, padx=10, pady=5)
entry_precio = tk.Entry(root)
entry_precio.grid(row=2, column=1)

tk.Button(root, text="Agregar", command=agregar_articulo).grid(row=3, column=0,pady=10)

tk.Button(root, text="Eliminar", command=eliminar_articulo).grid(row=3, column=1, pady=10)

lista_articulos = tk.Listbox(root, width=50, height=10)
lista_articulos.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Crear un botón y colocarlo en la ventana
btn_cerrar = tk.Button(root, text="Cerrar", command=cerrar)
btn_cerrar.grid(row=10, column=8, pady=5)
# Iniciar el bucle principal de la aplicación
root.mainloop()