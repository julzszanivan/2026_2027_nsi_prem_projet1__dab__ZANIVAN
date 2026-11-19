
import time



comptes_bancaires = {
    "123456": {
        "code": "4321",
        "solde": 1500,
        "plafond": 500,
        "plafond restant": 500,
        "historique": []
    },
    "654321": {
        "code": "0000",
        "solde": 45,
        "plafond": 200,
        "plafond restant": 200,
        "historique": []
    },
    "987654": {
        "code": "9999",
        "solde": 12000,
        "plafond": 1500,
        "plafond restant": 1500,
        "historique": []
    }
}


carte_inseree = None


essais_restants = 3

differents_billets = [100, 50, 20, 10]


def afficher(message, attente=1):
    print(message)
    time.sleep(attente)

def chargement(message, duree=2):
    print(message, end="", flush=True)
    for i in range(3):
        time.sleep(duree / 3)
        print(".", end="", flush=True)

    print()


def inserer_carte(numero_carte):
    global carte_inseree, essais_restants
    print("--- Insertion de la carte ---")
    if numero_carte in comptes_bancaires:
        afficher("Carte acceptée.", 1)
        chargement("Lecture de la puce", 2)
        carte_inseree = numero_carte
        essais_restants = 3
        afficher("Carte reconnue !", 1)
        return carte_inseree, essais_restants

    else:
        afficher("Erreur : Carte invalide ou non reconnue.")
        return None, 0


def authentifier(code_saisi):
    global carte_inseree, essais_restants
    if not carte_inseree:
        afficher("Aucune carte insérée.")
        return False
    compte = comptes_bancaires[carte_inseree]
    chargement("Vérification du code PIN", 2)
    if code_saisi == compte["code"]:
        afficher("Code PIN correct. Authentification réussie.")
        return True

    else:
        essais_restants -= 1
        afficher(f"Code PIN incorrect. Essais restants : {essais_restants}")
        if essais_restants == 0:
            afficher("Sécurité : Nombre d'essais maximal atteint.")
            afficher("Carte avalée, veuillez voir un de nos agents.")
            carte_inseree = None

        return False


def verifier_identite():
    global carte_inseree
    print("-- VERIFICATION DE SECURITE --")
    if carte_inseree is None:
        return False

    code = input("Veuillez confirmer votre code PIN : ")
    chargement("Vérification de votre identité", 2)
    compte = comptes_bancaires[carte_inseree]

    if code == compte["code"]:
        afficher("Identité confirmée.")
        afficher("Vous pouvez continuer.")
        return True

    else:
        afficher("Code PIN incorrect.")
        afficher("Votre carte est avalée.")
        afficher("Votre carte est conservée en sécurité à la banque.")
        afficher("Un message est envoyé à la banque.")

        carte_inseree = None
        return False


def avaler_carte():

    global carte_inseree

    print("\nAucune réponse détectée.")
    afficher("Votre carte est avalée.")
    afficher("Votre carte est conservée en sécurité à la banque.")
    afficher("Un message est envoyé à la banque.")

    carte_inseree = None
