import tkinter as tk
from tkinter.ttk import Notebook #https://www.youtube.com/watch?v=J48tIufwmRI&feature=youtu.be
import pathlib
from os import listdir

#https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
#https://www.youtube.com/watch?v=jBUpjijYtCk

from Classes.Windows.Window_MainPage import MainPage
from Classes.Windows.Window_StartPage import StartPage
from Classes.Windows.Window_RatioPage import RatioPage
from Classes.Windows.Window_GymPage import GymPage
from Classes.Windows.Window_PlayerPage import PlayerPage
from Classes.Windows.Window_MatchPage import MatchPage

# CONST
PATH_TO_APP = str(pathlib.Path(__file__).parent.absolute())

# https://www.tutorialspoint.com/python/python_gui_programming.htm

class Badmentrainement(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight = 5)
        container.grid_columnconfigure(0, weight = 5)

        self.frames = {}

        for F in (StartPage, MainPage, RatioPage, GymPage, PlayerPage, MatchPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

app1 = Badmentrainement()
app1.mainloop()

# Observer
def update_observer(*args):
    if var_gender.get():
        var_label_gender.set("C'est un homme")
    else:
        var_label_gender.set("C'est une femme")

def update_slider_label(*args):
    slider_label.set(slider_intvar.get())

#root = Tk()
#app = Window(root)
#root.mainloop()

app = tk.Tk()
app.geometry("400x300")
app.title("Un titre")
app.iconbitmap(PATH_TO_APP + r"\Sources\Images\shuttlecock_aWF_icon.ico" )

# Widgets
var_gender = tk.IntVar()
var_gender.trace_add("write", update_observer)
radio1 = tk.Radiobutton(app, text="Homme", value=1, variable=var_gender)
radio2 = tk.Radiobutton(app, text="Femme", value=0, variable=var_gender)
var_label_gender = tk.StringVar()
label_gender = tk.Label(app, textvariable=var_label_gender)

check_button = tk.Checkbutton(app, text="Publier", offvalue=2, onvalue=5)

slider_intvar = tk.IntVar()
slider_intvar.trace_add("write", update_slider_label)
slider = tk.Scale(app, activebackground="black", length=400, orient="horizontal", from_=0, to=100, tickinterval=10, label="Mon slider", variable=slider_intvar)
slider_label = tk.StringVar()
label_slider = tk.Label(app, textvariable=slider_label)


path_to_liste_fichier_liste_des_joueurs = PATH_TO_APP + r"\Sources\Listes_joueurs"
choix_liste_joueurs = tk.Listbox(app)
i = 0
for file_ in listdir(path_to_liste_fichier_liste_des_joueurs):
    i +=1
    choix_liste_joueurs.insert(i, file_)
choix_liste_joueurs.config(height=i)

radio1.pack()
radio2.pack()
label_gender.pack()
check_button.pack()
slider.pack()
label_slider.pack()
choix_liste_joueurs.pack()

Mainframe = tk.Frame(app)
Mainframe.pack(fill="both")  

tableLayout = Notebook(Mainframe)
#t1
tab1 = tk.Frame(tableLayout)
tab1.pack(fill="both")
labelt1 = tk.Label(tab1, text="coucou")
labelt1.pack()
tableLayout.add(tab1, text="TAB 1")
#t2
tab2 = tk.Frame(tableLayout)
tab2.pack(fill="both")
labelt2 = tk.Label(tab2, text="coucou2")
labelt2.pack()
tableLayout.add(tab2, text="TAB 2")
tableLayout.pack(fill="both")

app.mainloop()