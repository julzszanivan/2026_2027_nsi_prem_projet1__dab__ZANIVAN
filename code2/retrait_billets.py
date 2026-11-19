import time
from code2.compte_bancaire_identification import*
from code2.menu_programme import*

# ==========================================
# FONCTIONS DU RETRAIT
# ==========================================

def afficher_menu_retrait():

    print("===========")
    print("-- RETRAIT --")
    print("===========")


def demander_montant():

    # while True crée une boucle qui continue jusqu'à ce qu'on lui demande de s'arrêter.
    while True:
        try:
            # int() transforme la saisie en nombre entier.
            montant = int(input("Veuillez entrer un montant à retirer : "))
            return montant

        # except ValueError permet de gérer une erreur de saisie.
        except ValueError:
            afficher("Erreur : veuillez entrer un nombre entier.")


def verifier_montant(montant, plafond, solde):

    # On vérifie que le montant est supérieur à zéro.
    if montant <= 0:
        afficher("Erreur : le montant doit être supérieur à 0.")
        return False

    # % calcule le reste d'une division.
    # Si le reste est différent de zéro, le montant n'est pas divisible par 10.
    elif montant % 10 != 0:
        afficher("Erreur : le montant doit être divisible par 10.")
        return False

    # On vérifie que le retrait ne dépasse pas le plafond restant.
    elif montant > plafond:
        afficher(f"Erreur : votre plafond restant est de {plafond} €.")
        return False

    # On vérifie que le solde est suffisant.
    elif montant > solde:
        afficher("Erreur : solde insuffisant.")
        return False

    # Si aucune condition précédente n'est remplie, le montant est valide.
    return True


def effectuer_retrait(solde, montant):

    chargement("Traitement de votre demande", 2)
    chargement("Préparation des billets", 2)

    # On calcule le nouveau solde après le retrait.
    nouveau_solde = solde - montant

    afficher("Action réussie ! Votre retrait a été effectué.")
    afficher(f"Montant retiré : {montant} €")
    afficher(f"Votre nouveau solde est de : {nouveau_solde} €")

    return nouveau_solde


def retrait():

    # On récupère les informations du compte actuellement utilisé.
    compte = comptes_bancaires[carte_inseree]

    afficher_menu_retrait()

    # La boucle permet de redemander un montant si celui-ci est invalide.
    while True:

        montant = demander_montant()

        plafond = compte["plafond restant"]
        solde = compte["solde"]

        # On vérifie que le montant respecte toutes les conditions.
        if verifier_montant(montant, plafond, solde):

            nouveau_solde = effectuer_retrait(solde, montant)

            # On met à jour le solde et le plafond restant.
            compte["solde"] = nouveau_solde
            compte["plafond restant"] -= montant

            # append() ajoute une opération à la fin de la liste historique.
            compte["historique"].append(montant)

            # On appelle la fonction qui distribue les billets.
            billets(montant)

            # break permet de sortir de la boucle.
            break


# ==========================================
# FONCTION DU DEPOT
# ==========================================

def depot():

    compte = comptes_bancaires[carte_inseree]

    print("===========")
    print("-- DEPOT --")
    print("===========")

    while True:
        try:
            montant = int(input("Combien souhaitez-vous déposer ? "))

            if montant <= 0:
                afficher("Le montant doit être supérieur à 0.")

            elif montant % 10 != 0:
                afficher("Le montant doit être divisible par 10.")

            else:

                
                chargement("Insertion des billets", 2)
                chargement("Vérification des billets", 3)
                chargement("Analyse de l'authenticité des billets", 3)
                chargement("Comptage des billets", 2)

                afficher("Billets vérifiés !", 1)

                compte["solde"] += montant

                
                compte["historique"].append(-montant)

                afficher("Dépôt effectué avec succès !")
                afficher(f"Montant déposé : {montant} €")
                afficher(f"Nouveau solde : {compte['solde']} €")

                break

        except ValueError:
            afficher("Veuillez entrer un nombre entier.")


# ==========================================
# FONCTIONS DE DISTRIBUTION DES BILLETS
# ==========================================

def calculer_billets(montant, valeur_billet):

    # // effectue une division entière pour obtenir le nombre de billets.
    nombre_billets = montant // valeur_billet

    # % calcule le reste après avoir utilisé ces billets.
    reste = montant % valeur_billet

    return nombre_billets, reste


def afficher_billets(nombre, valeur):

    # On affiche uniquement les billets dont le nombre est supérieur à zéro.
    if nombre > 0:
        time.sleep(0.7)
        print(f"Voici {nombre} billet(s) de {valeur} €.")


def billets(montant_donne):

    print("===========")
    print("-- BILLETS --")
    print("===========")

    chargement("Distribution des billets", 2)

    # On parcourt chaque valeur de billet disponible.
    for valeur in differents_billets:

        # On calcule le nombre de billets et le montant restant.
        nombre, reste = calculer_billets(montant_donne, valeur)

        afficher_billets(nombre, valeur)

        # On remplace le montant initial par le reste à distribuer.
        montant_donne = reste

    # On vérifie s'il reste un montant impossible à distribuer.
    if montant_donne > 0:
        afficher("Impossible de distribuer la totalité du montant.")
