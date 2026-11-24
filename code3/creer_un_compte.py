from code3.depot import*

# ==========================================
# CREATION DE NOUVEAUX COMPTES
# ==========================================

def add_an_account(numero, cod, sold, plafond):

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

    numero_compte = str(random.randint(100000, 999999))

    while numero_compte in comptes_bancaires:
        numero_compte = str(random.randint(100000, 999999))

    return numero_compte


def code():

    code_pin = str(random.randint(1000, 9999))

    return code_pin


def solde():

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