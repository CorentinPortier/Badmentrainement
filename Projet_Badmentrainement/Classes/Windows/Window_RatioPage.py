import tkinter as tk

class RatioPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Ratio Page")
        label.pack()

        button = tk.Button(self, text = "Valider",
                           command = lambda: controller.show_frame("MainPage"))
        button.pack()