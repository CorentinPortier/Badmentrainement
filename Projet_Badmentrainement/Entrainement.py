import itertools
import random

class Entrainement(object):
    """Description"""
    def __init__(self, gymnase, participants):
        self.type_entrainement = self.demanderTypentrainement()
        self.gymnase = gymnase
        self.participants = participants
        #random.shuffle(self.participants)
        self.nb_participants = self.compterNbParticipants()
        self.liste_des_matchs = []

    def __str__(self):
        return "C'est un entrainement de type {}. Il se passe dans le gymnase \"{}\" à {}. Il y a {} participants.".format(self.type_entrainement,
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

    def compterNbParticipants(self):
        return len(self.participants)

    def calculerLesMatchs(self):
            return itertools.combinations(self.participants, 2)

    def afficherLesMatchs(self):
        self.liste_des_matchs = list(self.calculerLesMatchs())
        if(self.type_entrainement == "1v1"):
            for J in self.liste_des_matchs:
                print("{}({}) VS {}({})".format(J[0],J[0].ID, J[1], J[1].ID))
        if(self.type_entrainement == "2v2"):
            for j in range(int(len(self.liste_des_matchs)/2)):
                print(self.liste_des_matchs[j][0],"et", self.liste_des_matchs[j][1], "VS ", end = "")
                print(self.liste_des_matchs[-(j+1)][0], "et", self.liste_des_matchs[-(j+1)][1])