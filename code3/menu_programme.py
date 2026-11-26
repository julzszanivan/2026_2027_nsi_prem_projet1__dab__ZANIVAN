from code3.compte_bancaire_identification import*

# ==========================================
# FONCTIONS DU MENU PRINCIPAL
# ==========================================

def afficher_menu():
    """
    permet de demander a l'utilisateur ce qu'il veut faire entre consulter son solde, retirer de l'argent, consulter son historique, déposer de l'argent et quitter la session. On demande donc a l'utilisateur de choisir un nombre entre 1 et 5, si celui ci repond quelque chose d'autre le programme lui demande de remettre un nombre valide
    elle appelle la fonction retirer_carte, depot, consulter, afficher_historique
    elle est appelee par la

    """

    print("\n===========")
    print("-- MENU --")
    print("===========")

    print("1 - Consulter mon solde")
    print("2 - Retirer de l'argent")
    print("3 - Quitter")
    print("4 - Consulter mon historique")
    print("5 - Déposer de l'argent")

    debut_temps = time.time()

    try:
        nb = int(input("Choisissez une commande entre 1 et 5 : "))

    except ValueError:
        nb = 0

    duree = time.time() - debut_temps
    if duree > 15:

        print("\nAucune activité détectée.")
        print("Vérification de votre identité nécessaire.")

        if verifier_identite():
            return nb

        else:
            return -1

    if nb == 0:
        print("Veuillez entrer un nombre valide.")
        return 0

    if nb == 3:
        return 3

    return nb



def consulter():
    """
    permet a l'utilisateur de consulter son solde et le plafond qui lui reste 
    elle est appelee par la fonction afficher_menu
    """
    compte = comptes_bancaires[carte_inseree]

    chargement("Récupération des informations du compte", 2)

    solde = compte["solde"]
    plafond = compte["plafond restant"]

    afficher(f"Votre solde est de {solde} €")
    afficher(f"Votre plafond restant est de {plafond} €")


def afficher_historique():
    """
    permet a l'utilisateur de regarder son historique et si celui-ci n'a rien fait avant, le programme affiche aucune opération effectuée

    """

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