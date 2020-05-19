class Gymnase(object):
    """description of class"""
    def __init__(self, nom, liste_des_terrains, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_terrains = liste_des_terrains
        self.nb_t = self.compterNbTerrains()
    def compterNbTerrains(self):
        return len(self.liste_terrains)



