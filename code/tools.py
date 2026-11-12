import time

def afficher_menu():
    print("menu")
    print("commandes")
    print("1-consulter mon solde")
    print("2-retirer de l'argent")
    print("3-quitter")

    nb = int(input("Choisissez une commande entre 1 et 3 : "))

    if nb in [1, 2]:
        for i in range(3, -1, -1):
            time.sleep(15)

            print("Aucune activité détectée.")
            print("Êtes-vous toujours là ? Voulez-vous continuer ? (oui/non)")

            debut = time.time()

            reponse = input("Votre réponse : ").lower()

            duree = time.time() - debut

            if duree > 5:
                print("Aucune réponse détectée.")
                print("Carte avalée.")
                print("")
                print("Envoi d'un message.")
                break

            elif reponse in ["oui", "o"]:
                print("Retour au menu principal.")
                return afficher_menu()

            else:
                print("Veuillez reprendre votre carte.")
                break

    return nb