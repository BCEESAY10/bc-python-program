import tkinter as tk
from login_window import open_login_window
from register_window import open_register_window

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("BC TECH ACADEMY")
        self.geometry("450x300")
        self.config(bg='white')
        self.resizable(False, False)

        label = tk.Label(self, text="Hello, Welcome to BC Tech Academy!", font=('Anton', 20, 'bold'), bg='orange')
        label.pack()

        logoImage = tk.PhotoImage(file='Logo 4.png')
        logoLabel = tk.Label(self, image=logoImage)
        logoLabel.pack()

        controlFrame = tk.Frame(self)
        controlFrame.pack(pady=25)

        login_button = tk.Button(controlFrame, text="Login", font=('Arial', 18, 'bold'),
                                 cursor='hand2', bg='orange', command=self.open_login_window)
        login_button.pack(side=tk.LEFT, padx=10)

        register_button = tk.Button(controlFrame, text="Register", font=('Arial', 18, 'bold'),
                                    cursor='hand2', bg='orange', command=self.open_register_window)
        register_button.pack(side=tk.LEFT)

    def open_login_window(self):
        open_login_window(self)

    def open_register_window(self):
        open_register_window(self)

def login():
    print("Welcome to BC Tech")
