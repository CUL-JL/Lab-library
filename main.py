import tkinter as tk
from tkinter.messagebox import showerror
from controllers import LibraryController
from book import Book
# Crear la instancia del controlador
library = LibraryController()

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    recommendation = entry_recommendation.get() if include_recommendation.get() else "No aplica"

    if not (title and author and year):
        showerror("Error", "Por favor complete todos los campos.")
        return

    book = Book(title, author, year, recommendation)
    library.simple_list.add_book(book)

    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_recommendation.delete(0, tk.END)
    show_books()


def search_book():
    title = entry_search.get()
    if not title:
        showerror("Error", "Por favor ingrese un título para buscar.")
        return

    book = library.simple_list.search_title(title)
    if book:
        text_books.delete(1.0, tk.END)
        text_books.insert(tk.END, str(book))
    else:
        text_books.delete(1.0, tk.END)
        text_books.insert(tk.END, "Libro no encontrado.")


def delete_book():
    title = entry_search.get()
    if not title:
        showerror("Error", "Por favor ingrese un título para eliminar.")
        return

    book = library.simple_list.delete_book(title)
    if book:
        show_books()
        text_books.delete(1.0, tk.END)
        text_books.insert(tk.END, f"Se ha eliminado el libro: {book}")
    else:
        showerror("Error", "Libro no encontrado.")


def show_books():
    books = library.simple_list.show_books()
    text_books.delete(1.0, tk.END)
    text_books.insert(tk.END, books)

def toggle_recommendation_entry():
    if include_recommendation.get():
        entry_recommendation.config(state="normal")
    else:
        entry_recommendation.delete(0, tk.END)
        entry_recommendation.config(state="disabled")

root = tk.Tk()
root.title("Sistema de Reservación de Libros")
root.geometry("800x600")
root.configure(bg="lightblue")

frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tk.Label(frame, text="Nombre del Autor:", bg="lightblue").grid(row=0, column=0, padx=10, pady=10)
entry_author = tk.Entry(frame)
entry_author.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Titulo del libro:", bg="lightblue").grid(row=1, column=0, padx=10, pady=10)
entry_title = tk.Entry(frame)
entry_title.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame, text="Año de lanzamiento:", bg="lightblue").grid(row=2, column=0, padx=10, pady=10)
entry_year = tk.Entry(frame)
entry_year.grid(row=2, column=1, padx=10, pady=10)

tk.Label(frame, text="Recomendación del libro: del 1 al 5", bg="lightblue").grid(row=3, column=0, padx=10, pady=10)
entry_recommendation = tk.Entry(frame, state="disabled")  
entry_recommendation.grid(row=3, column=1, padx=10, pady=10)

include_recommendation = tk.BooleanVar()
tk.Checkbutton(frame, text="Incluir recomendación", variable=include_recommendation, bg="lightblue",
               command=toggle_recommendation_entry).grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(frame, text="Agregar libro", bg="green", fg="white", command=add_book).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

tk.Label(frame, text="Titulo del libro. Opciones:", bg="lightblue").grid(row=7, column=0, padx=10, pady=10)
entry_search = tk.Entry(frame)
entry_search.grid(row=7, column=1, padx=10, pady=10)

tk.Button(frame, text="Buscar", bg="green", fg="white", command=search_book).grid(row=8, column=0, columnspan=2, padx=10, pady=10)
tk.Button(frame, text="Eliminar libro", bg="red", fg="white", command=delete_book).grid(row=9, column=0, columnspan=2, padx=10, pady=10)

tk.Button(frame, text="Mostrar libros", bg="darkblue", fg="white", command=show_books).grid(row=10, column=0, columnspan=2, padx=10, pady=10)

text_books = tk.Text(frame, height=10, width=50)
text_books.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()