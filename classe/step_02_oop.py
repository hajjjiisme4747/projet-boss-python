class Tomobil:
    def __init__(self, lmarka):
        self.marka = lmarka       # Hada Attribut (Donnée)
        self.en_marche = False    # Hada Attribut (Donnée)

    def demarrer(self):           # Hadi Méthode (Action)
        self.en_marche = True

# 1. Kanbniw l'instance
tomo_1 = Tomobil("Dacia")

# 2. Kan9raw DONNÉE (Bla parenthèses)
print(tomo_1.marka)

# 3. Kandiro ACTION (B parenthèses)
tomo_1.demarrer()

# 4. Kan9raw DONNÉE jdida bach nchoufo wach l'action w93at
print(tomo_1.en_marche)