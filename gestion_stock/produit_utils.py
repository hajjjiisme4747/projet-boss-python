class Produit:
    total = 15

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
    def demande(self):
        if Produit.total > 0:
            print(f"la demande du produit : {self.nom} au prix : {self.prix} est bien confirme !")
            Produit.total -= 1
        else:
            print(f"le produit {self.nom} n'existe pas")
    @classmethod
    def stock(cls):
        return print(f"il reste {Produit.total} de ce produit dans le stock")