def division_pro(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        # Hna kankhedmou ghir ila b kanti kat'sawi 0
        return "Sme7 liya, ma'9dertch n'9ssem 3la zéro!"
    except TypeError:
        # Hna kankhedmou ila l'client dkhl texte f blasset raqm
        return "Khassk d'dkhel des chiffres a sidi!"
    else:
        # Had l'bloc khdam ghir ila l'Try daz 100% nja7
        print("L'calcul daz b naja7!")
        return resultat
    finally:
        # Dima khdam (Logging / Nettoyage)
        print("L'opération salat.")

print(division_pro(10, 0))
a = 10
b = 10
print(a.__add__(b))