def afficher_menu():
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    print("menu")
    print("commandes")
    print("1-consulter mon solde")
    print("2-retirer de l'argent")
    print("3-quitter")
    nb = int(input("choisissez une commande entre 1 et 3 , "))

    return nb 

 nb = afficher_menu()