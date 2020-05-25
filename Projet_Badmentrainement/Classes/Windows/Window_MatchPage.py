import tkinter as tk

class MatchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Match Page")
        label.pack()

        button = tk.Button(self, text = "Préparer le prochain round",
                           command = lambda: controller.show_frame("MainPage"))
        button.pack()