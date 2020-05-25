import tkinter as tk

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack()

        ratio_button = tk.Button(self, text = "Modifier le ratio",
                                 command = lambda: controller.show_frame("RatioPage"))
        gym_button = tk.Button(self, text = "Modifier le gymnase",
                                 command = lambda: controller.show_frame("GymPage"))
        player_button = tk.Button(self, text = "Ajouter un joueur",
                                 command = lambda: controller.show_frame("PlayerPage"))
        match_button = tk.Button(self, text = "Calculer le prochain round",
                                 command = lambda: controller.show_frame("MatchPage"))

        ratio_button.pack()
        gym_button.pack()
        player_button.pack()
        match_button.pack()