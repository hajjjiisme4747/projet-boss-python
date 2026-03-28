def ajouter_hacker(liste_utilisateurs):
    # La fonction reçoit un Post-it nommé 'liste_utilisateurs'
    # Ce Post-it est collé sur le MÊME OBJET en mémoire que la variable originale.

    print(f"[Dans la fonction] ID reçu : {id(liste_utilisateurs)}")

    # Puisque la liste est MUTABLE, on modifie l'objet physique directement !
    liste_utilisateurs.append("Hacker_1337")


# --- DANS NOTRE PROGRAMME PRINCIPAL ---
base_de_donnees = ["Alice", "Bob"]
print(f"[Avant fonction] ID original : {id(base_de_donnees)}")
print(f"[Avant fonction] Valeur : {base_de_donnees}")

# On envoie notre variable à la fonction
ajouter_hacker(base_de_donnees)

# Que va-t-il se passer ?
print(f"[Après fonction] Valeur : {base_de_donnees}")