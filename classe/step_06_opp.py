class CompteBancaire:
    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire  # Hadi variable Publique (M3erya)

        # HNA L'7IMAYA ! Derna '__' 9bel solde.
        # Daba wlat variable PRIVÉE (Mkhbya wast l'Class).
        self.__solde = solde_initial

        # ======================================================

    # Kifach l'client y9der ychouf flousso ila kant mkhbya ?
    # Kansawbo lih "Getter" (Action bach y9ra bla maybeddel)
    # ======================================================
    def get_solde(self):
        # L'Class ldakhel 3ndha l'7e9 tchouf '__solde'
        return self.__solde

    # ======================================================
    # Kifach l'client yzid l'flouss ?
    # Kansawbo lih "Setter" (Action kaddir l'contrôle 9bel matbeddel)
    # ======================================================
    def deposer_flouss(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Dazet {montant} DH b naja7.")
        else:
            print("ERREUR : Mat9derch tzid montant salib (Négatif) !")


# --- F ZZEN9A ---

compte_1 = CompteBancaire("Tariq", 1000)

# 1. Nchoufo l'variable publique
print(compte_1.titulaire)  # Ghadi t3tik "Tariq" (Khdama 100%)

# 2. L'Hacker bgha ychouf awla ybeddel l'variable Privée direct :

compte_1.__solde = 9999999

# 3. Tari9a char3iya (Légale) bach nkhdmo :
print(f"Solde dyali howa : {compte_1.get_solde()}")
compte_1.deposer_flouss(500)