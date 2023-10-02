import tkinter as tk
from tkinter import Frame, Entry, Label, Button, messagebox, Toplevel
from application import Application

def open_login_window(root):
    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.geometry("250x180")
    login_window.resizable(False, False)

    login_frame = Frame(login_window, padx=10)
    login_frame.grid(row=4, column=2)

    label_login = Label(login_frame, text="   LOGIN FORM", bg='orange', padx=15, pady=8, font=('Sans', 16, 'bold'))
    label_login.grid(row=1, column=1, columnspan=2)

    # ... (rest of the login window code)
