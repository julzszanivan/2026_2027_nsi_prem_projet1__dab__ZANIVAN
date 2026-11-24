from code3.depot import*

# ==========================================
# CREATION DE NOUVEAUX COMPTES
# ==========================================

def add_an_account(numero, cod, sold, plafond):
    """
    permet de rajouter un compte avec un code pin, un solde, un plafond. Lorsqu'il fera une action il y aura ainsi un plafond restant et un historique
    il prend en entrée: numero comme le numero de la carte, cod comme le code pin qui permettra de verifier son identité, sold comme le solde du compte, plafond comme le max d'argent qu'il puisse retirer durant la session
    """

    print("Création du compte en cours...")

    comptes_bancaires[numero] = {
        "code": cod,
        "solde": sold,
        "plafond": plafond,
        "plafond restant": plafond,
        "historique": []
    }

    print(f"Votre compte a été créé : ID : {numero}")
    print(f"Solde : {sold} €")
    print(f"Plafond : {plafond} €")
    print("merci de bien retenir vos identifiants")


def compte():
    """
    permet de creer un numero de compte aleatoire entre 100000 et 999999 qui n'existe pas encore 
    il est appele par la fonction add_an_account 
    """

    numero_compte = str(random.randint(100000, 999999))

    while numero_compte in comptes_bancaires:
        numero_compte = str(random.randint(100000, 999999))

    return numero_compte


def code():
    """
    permet de creer le code pin du compte
    il est appele par la fonction add_an_account 
    """

    code_pin = str(random.randint(1000, 9999))

    return code_pin


def solde():
    """
    permet a l'utilisateur de commencer avec de l'argent sur son compte, le systeme lui demande combien d'argent il veut placer sur son nouveau compte
    il est appele par la fonction add_an_account 
    """

    while True:
        try:
            montant = int(
                input(
                    "Combien d'argent voulez-vous placer sur votre "
                    "compte ? (entre 100 et 9 999 €) : "
                )
            )

            if 100 <= montant <= 9999:
                return montant

            else:
                print("Montant invalide. Entrez un montant entre 100 et 9 999 €.")

        except ValueError:
            print("Veuillez entrer un nombre entier.")