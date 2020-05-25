import numpy as np
import itertools
import math

from Classes.Program.Terrain import Terrain
from Classes.Program.Gymnase import Gymnase
from Classes.Program.Joueur import Joueur
from Classes.Program.Entrainement import Entrainement

liste_terrains = []
liste_terrains.append(Terrain("double"))
liste_terrains.append(Terrain("normal"))
liste_terrains.append(Terrain("simple"))
liste_terrains.append(Terrain("simple"))

gymnase_Annecy = Gymnase("Gymnase des Romains", liste_terrains, "Annecy")
for cle,val in gymnase_Annecy.terrains.items():
    print(cle, val)

liste_des_joueurs = []
liste_des_joueurs.append(Joueur("Audrey"))
liste_des_joueurs.append(Joueur("Corentin"))
liste_des_joueurs.append(Joueur("Corentin"))
liste_des_joueurs.append(Joueur("Nori"))
#liste_des_joueurs.append(Joueur("Navetodul"))
#liste_des_joueurs.append(Joueur("Cara"))

entrainement_A_Annecy = Entrainement(gymnase_Annecy, liste_des_joueurs)

print(entrainement_A_Annecy)

entrainement_A_Annecy.afficherTousLesMatchs()

for i in range(len(liste_des_joueurs)-1):
    print()
    entrainement_A_Annecy.calculerUnTour()

a,b = divmod(8,4)
print(a,b)
print(6-6%(4//2))

#b = [['' for x in range(len(a))] for y in range(len(a))]

#for e in b:
#    print(e)

#for i in range(len(a)):
#    for j in range(len(a)):
#        b[i][j] = a[i]+a[j]

#for e in b:
#    print(e)

#b = np.triu(b, k=1)

#for e in b:
#    print(e)

#marc = Joueur("Marc")
#jean = Joueur("Jean")
#print(marc.ID)
#print(jean.ID)
