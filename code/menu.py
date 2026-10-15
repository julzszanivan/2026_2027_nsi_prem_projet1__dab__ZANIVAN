" quand le client entre son code de carte il est dirigé sur ce menu"

def afficher_menu():
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print("menu")
    print("commandes")
    print("1-consulter mon solde")
    print("2-retirer de l'argent")
    print("3-quitter")
    nb = int(input("choisissez une commande entre 1 et 3 , "))

    return nb 

def consulter():
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print(f"le solde de votre compte est de {solde}€")


solde=300

nb = afficher_menu()
if nb == 1 :
    consulter()
elif nb == 2 :
    retirer()
elif nb == 3 :
    quitter
else  :
    print ("le nombre saisi est incorrect")

afficher_menu()

