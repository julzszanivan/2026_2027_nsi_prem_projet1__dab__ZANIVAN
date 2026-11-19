import time
from code2.compte_bancaire_identification import*
from code2.retrait_billets import*



def afficher_menu():

    print("\n===========")
    print("-- MENU --")
    print("==========")

    print("1 - Consulter mon solde")
    print("2 - Retirer de l'argent")
    print("3 - Quitter")
    print("4 - Consulter mon historique")
    print("5 - Déposer de l'argent")


    debut = time.time()

    try:
        nb = int(input("Choisissez une commande entre 1 et 5 : "))


    except ValueError:
        afficher("Veuillez entrer un nombre valide.")
        return 0

    duree = time.time() - debut


    if nb == 3:
        return 3

    if duree > 15:

        print("\nAucune activité détectée.")
        print("Vérification de votre identité nécessaire.")

        if verifier_identite():
            return nb

        else:
            return -1

    return nb


def consulter():

    compte = comptes_bancaires[carte_inseree]

    chargement("Récupération des informations du compte", 2)


    solde = compte["solde"]
    plafond = compte["plafond restant"]

    afficher(f"Votre solde est de {solde} €")
    afficher(f"Votre plafond restant est de {plafond} €")


def afficher_historique():

    compte = comptes_bancaires[carte_inseree]
    historique = compte["historique"]

    chargement("Chargement de votre historique", 2)

    print("============================")
    print("-- HISTORIQUE OPERATIONS --")
    print("============================")

    
    if len(historique) == 0:
        afficher("Aucune opération effectuée.")

    else:
        
        for montant in historique:

            time.sleep(0.7)

            
            if montant > 0:
                print(f"Retrait de {montant} €")

            else:
                print(f"Dépôt de {-montant} €")




def retirer_carte():

    global carte_inseree

    chargement("Fermeture de votre session", 2)

    afficher("Veuillez récupérer votre carte.")


    carte_inseree = None

    afficher("Merci de votre visite !")



while True:

    print("\n================================")
    print("     DISTRIBUTEUR BANCAIRE")
    print("================================\n")

    numero_carte = input("Veuillez insérer votre carte : ")

   
    inserer_carte(numero_carte)

    
    if carte_inseree is None:
        afficher("Veuillez utiliser une carte valide.", 1)
        continue


    authentifie = False


    while essais_restants > 0 and not authentifie:

        code = input("Veuillez saisir votre code PIN : ")
        authentifie = authentifier(code)

    
    if not authentifie:
        afficher("Fin de la session.", 1)
        continue

    chargement("Connexion à votre compte bancaire", 2)

    afficher("Bienvenue dans votre espace bancaire !")

  
    while carte_inseree is not None:

        nb = afficher_menu()

        
        if nb == -1:
            retirer_carte()
            break

      

        elif nb == 1:
            consulter()

        elif nb == 2:
            retrait()

        elif nb == 3:
            retirer_carte()
            break

        elif nb == 4:
            afficher_historique()

        elif nb == 5:
            depot()

        else:
            afficher("Le nombre saisi est incorrect.")
