# 1. L'Class Parent (L'Abb) - Fiha l'hwayj l'mchtarka
class Vehicule:
    def __init__(self, marka):
        self.marka = marka
        self.vitesse = 0

    def klaxonner(self):
        print(f"[{self.marka}] kaddir : Tiiiiiit Tiiiiit !")


# 2. L'Class Enfant (L'Weld) - Tomobil katwret mn Vehicule
# Kankhesouh bin 9awsayn (Vehicule) bach Python y3ref chkoun hwa l'abb
class Tomobil(Vehicule):
    def __init__(self, marka, nombre_biban):
        # super() kat3ni : "Sir l3nd l'Abb (Vehicule) w khdem l'__init__ dyalo"
        # Hakda, l'abb kaywjed lina 'marka' w 'vitesse' bla man3awdo nktbohom !
        super().__init__(marka)

        # W hna kanzido l'khassiya jdida lli kayna GHIR f tomobil
        self.nombre_biban = nombre_biban

    # L'weld y9der yzid actions jdad dyalo rasso
    def ch3el_climatiseur(self):
        print("Climatiseur khdam, brrr ❄️")


# --- F ZZEN9A (L'Exécution) ---

tomo_1 = Tomobil("Dacia", 4)

# Tomobil werta 'klaxonner' mn 3nd Vehicule, wakha makatbinhach west Tomobil !
tomo_1.klaxonner()
tomo_1.ch3el_climatiseur()
print(f"Tomobil fiha {tomo_1.nombre_biban} biban.")