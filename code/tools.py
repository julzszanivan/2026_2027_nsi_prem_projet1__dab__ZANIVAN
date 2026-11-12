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




def verifier_identite():

    global carte_inseree
    print("-- VERIFICATION DE SECURITE --")
    code = input("Veuillez confirmer votre code PIN : ")
    if carte_inseree is None:
        return False

    compte = comptes_bancaires[carte_inseree]
    if code == compte["code"]:
        print("Identité confirmée.")
        print("Vous pouvez continuer.")
        return True
    else:
        print("Code PIN incorrect.")
        print("Votre carte est avalée.")
        print("Votre carte est conservée en sécurité à la banque.")
        print("Un message est envoyé à la banque.")
        carte_inseree = None
        return False


def avaler_carte():
    global carte_inseree
    print("\nAucune réponse détectée.")
    print("Votre carte est avalée.")
    print("Votre carte est conservée en sécurité à la banque.")
    print("Un message est envoyé à la banque.")

    carte_inseree = None
