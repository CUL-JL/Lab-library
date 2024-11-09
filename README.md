# Lab: Creating a Library with Linked Lists

This project consists of creating a Python program that simulates a library through a graphical user interface (GUI) using `Tkinter`. The program allows managing books, storing them in lists, and performing various operations on them such as adding, searching, deleting, and displaying books.

## Requirements

### 1. **Books**:
Each book has the following attributes:
- **Title**: Name of the book.
- **Author**: Author of the book.
- **Publication Year**: Year the book was published.
- **Recommendation**: Recommendation level of the book (from 1 to 5).

### 2. **Lists**:

The library system implements different types of lists:
- **Simple List**: Books are stored in the order they are added.

## Available Operations

The program allows the following operations:

1. **Add a book**:
   - A book can be added by providing the title, author, publication year, and optionally, a recommendation (from 1 to 5).

2. **Search for a book**:
   - A book can be searched by its title in the simple list.

3. **Delete a book**:
   - A book can be deleted from the simple list by providing the title.

4. **Show all books**:
   - A complete list of the currently stored books is displayed.

## Code Structure

The program is structured as follows:

### **Main file:**

```python
import tkinter as tk
from tkinter.messagebox import showerror
from controllers import LibraryController
from book import Book

# Create the controller instance
library = LibraryController()

def add_book():
    # Code to add a book
    ...

def search_book():
    # Code to search for a book by title
    ...

def delete_book():
    # Code to delete a book by title
    ...

def show_books():
    # Code to show the books
    ...

def toggle_recommendation_entry():
    # Enable or disable the recommendation entry
    ...

# GUI configuration with Tkinter
root = tk.Tk()
root.title("Book Reservation System")
root.geometry("800x600")
root.configure(bg="lightblue")

frame = tk.Frame(root, bg="lightblue")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Entry fields for Author, Title, Publication Year, and Recommendation
...

# Buttons to add, search, delete, and show books
...

# Text widget to display results
text_books = tk.Text(frame, height=10, width=50)
text_books.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()