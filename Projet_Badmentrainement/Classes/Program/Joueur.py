class Joueur(object):
    ID = 0
    """Joueur possédant un ID, un nom, une liste d'adversaire et un opposant"""
    def __init__(self, name):
        Joueur.ID += 1
        self.name = name
        self.ID = Joueur.ID
        self.adversaires = []
        self.opposant = None
        self.S = 0
        self.D = 0
    def __str__(self):
        return self.name + "("+str(self.ID)+")"

    def setOpposant(self, opposant):
        self.opposant = opposant
        opposant.opposant = self
        self.adversaires.append(opposant)
        opposant.adversaires.append(self)





