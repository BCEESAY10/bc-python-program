import tkinter as tk
from tkinter import Frame, Entry, Label, Button, Toplevel
from application import Application

entry_widgets = []

def register():
    for entry in entry_widgets:
        if entry.get() == "":
            messagebox.showerror("error", "Please fill all entries")
            return
    messagebox.showinfo("message", "Successfully registered")

def open_register_window(root):
    global entry_widgets
    register_window = Toplevel(root)
    register_window.title("Register")
    register_window.geometry("200x320")
    register_window.resizable(False, False)

    entry_frame = Frame(register_window, padx=10)
    entry_frame.pack()

    labels = ["Full Name:", "Phone Number:", "Password:", "Address:", "Date of Birth:", "Program interested:"]
    for label_text in labels:
        label = Label(entry_frame, text=label_text)
        label.pack()
        entry = Entry(entry_frame)
        entry.pack()
        entry_widgets.append(entry)

    register_button = Button(entry_frame, text="Register", command=register)
    register_button.pack()
