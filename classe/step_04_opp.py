class Utilisateur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

user_1 = Utilisateur("Tariq", "tariq@gmail.com")
print(user_1)