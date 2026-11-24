from code3.retirer_carte import*

# ==========================================
# FONCTIONS DU RETRAIT
# ==========================================

def afficher_menu_retrait():
    print("===========")
    print("-- RETRAIT --")
    print("===========")


def demander_montant():

    while True:
        try:
            montant = int(
                input("Veuillez entrer un montant à retirer : ")
            )
            return montant

        except ValueError:
            afficher("Erreur : veuillez entrer un nombre entier.")


def verifier_montant(montant, plafond, solde):

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

    chargement("Traitement de votre demande", 2)
    chargement("Préparation des billets", 2)

    nouveau_solde = solde - montant

    afficher("Action réussie ! Votre retrait a été effectué.")
    afficher(f"Montant retiré : {montant} €")
    afficher(f"Votre nouveau solde est de : {nouveau_solde} €")

    return nouveau_solde


def retrait():

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

    nombre_billets = montant // valeur_billet
    reste = montant % valeur_billet

    return nombre_billets, reste


def afficher_billets(nombre, valeur):

    if nombre > 0:
        time.sleep(0.7)
        print(f"Voici {nombre} billet(s) de {valeur} €.")


def billets(montant_donne):

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