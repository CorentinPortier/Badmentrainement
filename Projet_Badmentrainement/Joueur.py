class Joueur(object):
    ID = 0
    """description of class"""
    def __init__(self, name):
        Joueur.ID += 1
        self.name = name
        self.ID = Joueur.ID
        self.adversaires = []
        self.opposant = None
    def __str__(self):
        return str(self.ID) + self.name





