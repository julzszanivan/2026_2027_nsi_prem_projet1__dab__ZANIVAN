from code3.creer_un_compte import*

# ==========================================
# DEBUT DU PROGRAMME
# ==========================================

def debut():
    """
    permet a l'utilisateur de choisir entre se creer un compte si il n'en a pas ou de rentrer son numerop de carte si il en a un. l'utiliateur choisi entre le nombre 1 et 0. si il a un compte il doit ecrire son code pin. si il n'a pas de compte la fonction add_an_account est appelee
    """

    print("\n================================")
    print("     DISTRIBUTEUR BANCAIRE")
    print("================================\n")

    while True:
        try:
            rep = int(input(
                "Avez-vous déjà un compte ? (0 : non ; 1 : oui) : "
            ))

            if rep == 0:

                numero = compte()
                cod = code()
                sold = solde()
                plafond = 500

                add_an_account(numero, cod, sold, plafond)

                print("\nVotre numéro de carte est :", numero)
                print("Votre code PIN est :", cod)

                inserer_carte(numero)
                return True

            elif rep == 1:

                numero_carte = input(
                    "Veuillez insérer votre numéro de carte : "
                )

                return inserer_carte(numero_carte)[0] is not None

            else:
                print("Réponse incorrecte.")

        except ValueError:
            print("Veuillez saisir 0 ou 1.")


# ==========================================
# PROGRAMME PRINCIPAL
# ==========================================

while True:

    if not debut():
        continue

    authentifie = False

    while essais_restants > 0 and not authentifie:

        code_saisi = input("Veuillez saisir votre code PIN : ")
        authentifie = authentifier(code_saisi)

    if not authentifie:
        afficher("Fin de la session.", 1)
        continue

    chargement("Connexion à votre compte bancaire", 2)
    afficher("Bienvenue dans votre espace bancaire !")

    while carte_inseree is not None:

        nb = afficher_menu()

        if nb == -1:
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
