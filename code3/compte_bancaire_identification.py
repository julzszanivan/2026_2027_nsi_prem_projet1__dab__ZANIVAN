import time
import random

# ==========================================
# BASE DE DONNEES DES COMPTES BANCAIRES
# ==========================================

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


# ==========================================
# ETAT DE LA SESSION
# ==========================================

carte_inseree = None
essais_restants = 3

differents_billets = [100, 50, 20, 10]

# ==========================================
# FONCTIONS D'AFFICHAGE ET D'ATTENTE
# ==========================================

def afficher(message, attente=1):
    """
    permet pour chaque message afficher de faire une courte pause en prenant le message et l'attente voulu pour ne pas envoyer trop de message rapidement
    il prend en entre le message et l'attente voulu
    """
    print(message)
    time.sleep(attente)


def chargement(message, duree=2):
    """
    permet de faire une attente avant d'afficher le message pour que ce soit plus réaliste
    il prend en entre le message et l'attente voulu
    """
    print(message, end="", flush=True)

    for i in range(3):
        time.sleep(duree / 3)
        print(".", end="", flush=True)

    print()


# ==========================================
# FONCTIONS DE LA CARTE BANCAIRE
# ==========================================

def inserer_carte(numero_carte):
    """
    cette fonction sert a verifier la carte de mis par l'utilisateur
    elle prend en entre le numero de carte de l'utilisateur taper au prealable par l'input veuillez insere votre carte
    elle change carte inserer pour dir qu'il y en a une sinon si C faut il y a pas de carte et pas de chance pour leverifier le code pin
    """
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
        carte_inseree = None
        return None, 0


def authentifier(code_saisi):
    """
    verifie le code de la carte si y a, et enleve 1 essai par erreur de code jusqua 3 essairater, s'il n'y a pas d'essai restant alors la carte est avalée
    elle prend en entre le code saisi dans le while true de programme principale
    """
    global carte_inseree, essais_restants

    if carte_inseree is None:
        afficher("Aucune carte insérée.")
        return False

    compte = comptes_bancaires[carte_inseree]

    chargement("Vérification du code PIN", 2)

    if code_saisi == compte["code"]:
        afficher("Code PIN correct. Authentification réussie.")
        return True

    else:
        essais_restants -= 1

        afficher(
            f"Code PIN incorrect. Essais restants : {essais_restants}"
        )

        if essais_restants == 0:
            afficher("Sécurité : Nombre d'essais maximal atteint.")
            afficher("Carte avalée, veuillez voir un de nos agents.")
            carte_inseree = None

        return False


def verifier_identite():
    """"
    permet de verifier si C encore le meme utilisateur qui a mis sa carte que celui qui est derriere la borne. il vgerifie donc le code pin si C le bbon alors l'action continue et si C faut y a un message qui dit que sa carte est avaler et conserve a la banque
    elle est appeler lorsque l'utilisateur a mis plus de 20 seconde sans rien faire dans le menue
    """
    global carte_inseree

    print("-- VERIFICATION DE SECURITE --")

    if carte_inseree is None:
        return False

    code_saisi = input("Veuillez confirmer votre code PIN : ")

    chargement("Vérification de votre identité", 2)

    compte = comptes_bancaires[carte_inseree]

    if code_saisi == compte["code"]:
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
