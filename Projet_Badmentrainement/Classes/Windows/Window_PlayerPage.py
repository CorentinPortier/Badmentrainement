import tkinter as tk

class PlayerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Player Page")
        label.pack()

        button = tk.Button(self, text = "Valider",
                           command = lambda: controller.show_frame("MainPage"))
        button.pack()