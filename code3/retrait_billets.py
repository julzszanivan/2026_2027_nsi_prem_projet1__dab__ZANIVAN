from code3.retirer_carte import*

# ==========================================
# FONCTIONS DU RETRAIT
# ==========================================

def afficher_menu_retrait():
    """
    permet d'afficher retrait pour que l'utilisateur sache ou il est
    """
    print("===========")
    print("-- RETRAIT --")
    print("===========")


def demander_montant():
    """
    permet de demander a l'utilisateur combien il veut retirer et que ce nombre est bien un nombre entier
    cette fonction est appelee par verifier_montant
    """

    while True:
        try:
            montant = int(
                input("Veuillez entrer un montant à retirer : ")
            )
            return montant

        except ValueError:
            afficher("Erreur : veuillez entrer un nombre entier.")


def verifier_montant(montant, plafond, solde):
    """
    premet de verifier que toutes les conditions du retrait sont remplies: un nombre superieur a 0, divisible par 10, et inferieur ou egale au plafond et au solde
    elle appelle la fonction demander_montant
    """

    if montant <= 0:
        afficher("Erreur : le montant doit être supérieur à 0.")
        return False

    elif montant % 10 != 0:
        afficher("Erreur : le montant doit être divisible par 10.")
        return False

    elif montant > plafond:
        afficher(f"Erreur : votre plafond restant est de {plafond} €.")
        return False

    elif montant > solde:
        afficher("Erreur : solde insuffisant.")
        return False

    return True


def effectuer_retrait(solde, montant):
    """
    permet de donner le montant a l'utilisateur et de monter son nouveau solde et ce qu'il a retire
    """

    chargement("Traitement de votre demande", 2)
    chargement("Préparation des billets", 2)

    nouveau_solde = solde - montant

    afficher("Action réussie ! Votre retrait a été effectué.")
    afficher(f"Montant retiré : {montant} €")
    afficher(f"Votre nouveau solde est de : {nouveau_solde} €")

    return nouveau_solde


def retrait():
    """
    permet de changer dans le dictionnaire le solde, le plafond restant et l'historique
    """

    compte = comptes_bancaires[carte_inseree]

    afficher_menu_retrait()

    while True:

        montant = demander_montant()

        plafond = compte["plafond restant"]
        solde = compte["solde"]

        if verifier_montant(montant, plafond, solde):

            nouveau_solde = effectuer_retrait(solde, montant)

            compte["solde"] = nouveau_solde
            compte["plafond restant"] -= montant

            compte["historique"].append(montant)

            billets(montant)

            break

# ==========================================
# FONCTIONS DE DISTRIBUTION DES BILLETS
# ==========================================

def calculer_billets(montant, valeur_billet):
    """
    permet de calculer le nombre de billets d'une valeur donnee ainsi que le montant restant à distribuer
    elle est appelee par la fonction afficher_billets
    """

    nombre_billets = montant // valeur_billet
    reste = montant % valeur_billet

    return nombre_billets, reste


def afficher_billets(nombre, valeur):
    """
    montre a l'utilisateur quel(s) billet(s) il recevra
    elle appelle la fonction calculer_billets
    """
    if nombre > 0:
        time.sleep(0.7)
        print(f"Voici {nombre} billet(s) de {valeur} €.")


def billets(montant_donne):
    """
    permet de calculer les billets à distribuer à l'utilisateur selon le montant demande
    """

    print("===========")
    print("-- BILLETS --")
    print("===========")

    chargement("Distribution des billets", 2)

    for valeur in differents_billets:

        nombre, reste = calculer_billets(
            montant_donne, valeur
        )

        afficher_billets(nombre, valeur)

        montant_donne = reste

    if montant_donne > 0:
        afficher("Impossible de distribuer la totalité du montant.")