import numpy as np
import itertools

from Terrain import Terrain
from Gymnase import Gymnase
from Joueur import Joueur
from Entrainement import Entrainement

liste_terrains = []
liste_terrains.append(Terrain("double"))
liste_terrains.append(Terrain("simple"))
liste_terrains.append(Terrain("double"))

gymnase_Annecy = Gymnase("Gymnase des Romains", liste_terrains, "Annecy")

liste_des_joueurs = []
liste_des_joueurs.append(Joueur("Audrey"))
liste_des_joueurs.append(Joueur("Corentin"))
liste_des_joueurs.append(Joueur("Corentin"))
liste_des_joueurs.append(Joueur("Nori"))
#liste_des_joueurs.append(Joueur("Navetodul"))

entrainement_A_Annecy = Entrainement(gymnase_Annecy, liste_des_joueurs)

print(entrainement_A_Annecy)

for elt in entrainement_A_Annecy.participants:
    print(elt.ID, elt.name)

entrainement_A_Annecy.afficherLesMatchs()


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