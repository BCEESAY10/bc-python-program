import tkinter as tk
from tkinter import messagebox
from login_window import open_login_window
from register_window import open_register_window
from application import Application

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

if __name__ == "__main__":
    main()
