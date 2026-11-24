from code3.compte_bancaire_identification import*

# ==========================================
# FONCTIONS DU MENU PRINCIPAL
# ==========================================

def afficher_menu():

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
        afficher("Veuillez entrer un nombre valide.")
        return 0

    duree = time.time() - debut_temps

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