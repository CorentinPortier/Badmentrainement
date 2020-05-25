class Gymnase(object):
    """description of class"""
    def __init__(self, nom, liste_des_terrains, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_terrains = liste_des_terrains
        self.nb_terrains = len(self.liste_terrains)
        self.terrains = {"N" : 0, "S": 0, "D": 0}

        for terrain in self.liste_terrains:
            if(terrain.taille == "normal"):
                self.terrains["N"] += 1
            elif(terrain.taille == "simple"):
                self.terrains["S"] += 1
            elif(terrain.taille == "double"):
                self.terrains["D"] += 1



