import tkinter as tk
from tkinter import messagebox

def create_window(title, width=300, height=200, allow_resize_width=True, allow_resize_height=True, center_window_on_screen=True):
    """Create a Tkinter window with the specified title and size."""
    window = tk.Tk()
    window.title(title)
    window.resizable(allow_resize_width, allow_resize_height)
    window.geometry(f"{width}x{height}")
    
    if center_window_on_screen == True:
        center_window(window)

    return window

def Add_label(window, text, x=0, y=0):
    """Add a label to the window."""
    label = tk.Label(window, text=text)
    label.place(x=x, y=y)

    return label

def Add_entry(window, x=0, y=0):
    """Add an entry field to the window."""
    entry = tk.Entry(window)
    entry.place(x=x, y=y)

    return entry

def add_combobox(window, values, x=0, y=0):
    """Add a combobox to the window."""
    combobox = tk.ttk.Combobox(window, values=values)
    combobox.place(x=x, y=y)

    return combobox

def Add_button(window, text, command, x=0, y=0):
    """Add a button to the window."""
    button = tk.Button(window, text=text, command=command)
    button.place(x=x, y=y)

    return button

def get_widget_size(widget):
    """Get the size of a widget."""

    width = widget.winfo_width()
    height = widget.winfo_height()

    return (width, height)

def center_window(window):
    """Center the window on the screen."""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def show_message(title, message):
    """Show a message box."""
    messagebox.showinfo(title, message)