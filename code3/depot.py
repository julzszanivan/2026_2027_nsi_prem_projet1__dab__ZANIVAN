from code3.retrait_billets import*

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
            montant = int(
                input("Combien souhaitez-vous déposer ? ")
            )

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