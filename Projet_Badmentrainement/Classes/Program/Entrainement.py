import itertools
import random

class Entrainement(object):
    """Description"""
    NbDeTours = 0
    def __init__(self, gymnase, participants):
        self.type_entrainement = self.demanderTypentrainement()
        self.ratio = self.demanderRatio()
        self.gymnase = gymnase
        self.participants = participants
        #random.shuffle(self.participants)
        self.nb_participants = len(self.participants)
        self.liste_des_matchs = []
        self.liste_choix_possible = []

    def __str__(self):
        return "\nC'est un entrainement de type {}. Il se passe dans le gymnase \"{}\" à {}. Il y a {} participants.\n".format(self.type_entrainement,
                                                                                                                   self.gymnase.nom, 
                                                                                                                   self.gymnase.adresse,
                                                                                                                   self.nb_participants)
    def demanderTypentrainement(self):
        choix_valide = False
        while( not choix_valide):
            type_entrainement = input("Type d'entrainement ? 2v2 ? 1v1 ?\n")
            if(type_entrainement == "1v1" or type_entrainement == "2v2"):
                choix_valide = True
            else:
                print("Veuillez choisir entre \"1v1\" et \"2v2\"")
        return type_entrainement
    def demanderRatio(self):
        return 100

    def afficherTousLesMatchs(self):
        self.liste_des_matchs = list(itertools.combinations(self.participants, 2))
        if(self.type_entrainement == "1v1"):
            for J in self.liste_des_matchs:
                print("{} VS {}".format(J[0], J[1]))
        if(self.type_entrainement == "2v2"):
            for j in range(int(len(self.liste_des_matchs)/2)):
                print(self.liste_des_matchs[j][0],"et", self.liste_des_matchs[j][1], " VS ", end = "")
                print(self.liste_des_matchs[-(j+1)][0], "et", self.liste_des_matchs[-(j+1)][1])

    def calculerUnTour(self):
        Entrainement.NbDeTours += 1;
        print("### Round " + str(Entrainement.NbDeTours) +" ###")
        joueurs = self.participants.copy()
        if(len(joueurs)%2 == 0):
            while(len(joueurs) != 0):
                J = joueurs.pop(0)
                if(J.opposant == None):
                    for joueur in joueurs:
                        if(J.ID != joueur.ID):
                            if(joueur not in(J.adversaires)):
                                J.setOpposant(joueur)
                                joueurs.remove(joueur)
                                print("{} joue contre {}".format(J, J.opposant))
                                break;
            self.resetOpposants()
            self.checkToutLeMondeAJouerContreToutLeMonde()
        else:
            print("Nombre impair de joueurs. :àfaire:")

    def resetOpposants(self):
        for J in self.participants:
            J.opposant = None

    def checkToutLeMondeAJouerContreToutLeMonde(self):
        for J in self.participants:
            if(len(J.adversaires) == len(self.participants)-1): # -1 car un joueur ne peut pas jouer contre lui même °°
                print("{} a joué contre tout le monde !".format(J))