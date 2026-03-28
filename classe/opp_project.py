class Documente:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.__est_emprunte = False

    def verifier_disponibilite(self):
        return self.__est_emprunte

    def changer_statut(self):
        self.__est_emprunte = not self.__est_emprunte

    def __str__(self):
        return f'"{self.titre}" par {self.auteur}'

class Livre(Documente):
    def __init__(self, titre, auteur, nombres_pages):
        super().__init__(titre, auteur)
        self.nombres_pages = nombres_pages


class Membre:
    # 1. Had variable mcharka f l'Class kamla (Sbboura)
    total_membres = 0

    # 2. __init__ dima kakhod 'self' (machi cls) w dima Bla Tarboch (@)
    def __init__(self, nom):
        # Attribut d'instance 3adi
        self.nom = nom

        # Attribut d'instance PRIVÉ (Liste khawya d l'ktob)
        # Had l'variable khassa b kol membre bo7do
        self.__livres_empruntes = []

        # 3. HNA L'MAGIE : Kanmchiw l l'Class 'Membre' nishaan
        # w kanzidu 1 f l'variable l'mcharka
        Membre.total_membres += 1

    # Mission 4 : Action bach ntselfu ktab
    def emprunter_livre(self, livre):
        # Khasna nchoufu wach l'ktab disponible (khdem l'action li sawbti f Document)
        if not livre.verifier_disponibilite():  # mnin katsawb l'action katrje3 False ila ktab disponible (7it __est_emprunte = False)
            livre.changer_statut()  # nreddouh True (mssellet)
            self.__livres_empruntes.append(livre)  # nzidouh f l'liste dyal l'client
            print(f"{self.nom} a emprunté {livre.titre}")
        else:
            print(f"Désolé, {livre.titre} est déjà emprunté.")

    @classmethod
    def afficher_total(cls):
        # Hna khedemna @classmethod 7it bghina ghir nchoufu raqm l'global
        print(f"Total des membres : {cls.total_membres}")


# 1. Création d'un livre
l1 = Livre("Python Master", "Tariq", 300)

# 2. Création d'un membre
m1 = Membre("Ayoub")

# 3. Test de l'emprunt
m1.emprunter_livre(l1)

# 4. Vérifier si le livre est indisponible après l'emprunt
print(f"Disponibilité de {l1.titre} : {l1.verifier_disponibilite()}")