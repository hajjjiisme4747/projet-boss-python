class Utilisateur:
    # Attribut mcharek (compteur global)
    total_users = 0

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Utilisateur.total_users += 1

    # ========================================================
    # POUVOIR 1 : Lire wa7ed l'information globale bla objet
    # ========================================================
    @classmethod
    def afficher_statistiques(cls):
        # Limite : Hna man9derch ndir print(cls.nom) -> ERREUR !
        print(f"Total des utilisateurs f la base : {cls.total_users}")

    # ========================================================
    # POUVOIR 2 (LE VRAI POUVOIR) : L'Usine Alternative
    # Kifach nsawbo Utilisateur mn texte mlassa9 "Tariq-25" ?
    # ========================================================
    @classmethod
    def creer_depuis_texte(cls, texte_bizarre):
        # 1. Kanfer9o l'texte 3la 2 blassa d'tiré '-'
        # result =["Tariq", "25"]
        donnees = texte_bizarre.split('-')
        nom_jdid = donnees[0]
        age_jdid = donnees[1]

        # 2. HNA L'MAGIE ! 'cls' hiya L'Class 'Utilisateur'.
        # Mnin kandir cls(nom, age) b7al ila drt Utilisateur(nom, age) !
        # Donc had l'action katbni lina instance jdida w kat3tiha lina (return).
        return cls(nom_jdid, age_jdid)


# --- F ZZEN9A ---

# Pouvoir 1 : Kan9raw l'compteur 9bel maykoun 7ta objet
Utilisateur.afficher_statistiques()

# Kanbniw objet b tari9a l'3adiya (__init__)
user1 = Utilisateur("Ayoub", 30)

# POUVOIR 2 : Kanbniw objet jdiiiid b tari9a l'alternative (@classmethod)
# Chouf mzyan hna : V2 radi tweli INSTANCE 7a9i9iya,
# 7it l'action 'creer_depuis_texte' fiha 'return cls(...)' l'dakhel !
user2 = Utilisateur.creer_depuis_texte("Tariq-25")

print(f"User 2 smito : {user2.nom} w f 3mro {user2.age} ans.")

# Kan3awdo nchoufo l'compteur
Utilisateur.afficher_statistiques()


# 1. On crée notre décorateur (Le videur)
def videur_de_boite(fonction_page_secrete):
    # On crée une fonction interne qui va faire la vérification
    def verification():
        print("HALTE ! Est-ce que tu es connecté ?")
        # Ici on pourrait mettre une vraie condition (if utilisateur_connecte:)
        print("C'est bon, tu peux passer.")

        # On exécute enfin la vraie fonction
        fonction_page_secrete()

    # Le décorateur renvoie la fonction modifiée
    return verification


# 2. On utilise le décorateur avec le symbole @
@videur_de_boite
def afficher_page_secrete():
    print("Bienvenue sur la page secrète de Django !")


# 3. On teste :
afficher_page_secrete()

